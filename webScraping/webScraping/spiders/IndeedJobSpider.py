import re
import json
import scrapy
from urllib.parse import urlencode

class IndeedJobSpider(scrapy.Spider):
    name = "indeedSpider"

    '''
        @Author: @DeanLogan
        @Description: Constructs an Indeed search URL for a given keyword, location, and offset.
        @param keyword: The keyword for the job search.
        @param location: The location for the job search.
        @param offset: The starting offset for paginating through job results (default is 0).
        @return: The constructed Indeed search URL.
    '''
    def getIndeedSearchUrl(self, keyword, location, offset=0):
        # Helper function to construct the Indeed search URL
        parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
        return "https://www.indeed.com/jobs?" + urlencode(parameters)

    '''
        @Author: @DeanLogan
        @Description: Generates start requests for job search using specified keywords and locations.
        @return: A sequence of requests for each combination of keyword and location.
    '''
    def start_requests(self):
        # List of keywords and locations to search for jobs
        keywordList = ['data analyst']
        locationList = ['Belfast']

        # Generate requests for each combination of keyword and location
        for keyword in keywordList:
            for location in locationList:
                indeedJobsUrl = self.getIndeedSearchUrl(keyword, location)

                # Yield a request with the 'parseSearchResults' callback
                yield scrapy.Request(url=indeedJobsUrl, callback=self.parseSearchResults, meta={'keyword': keyword, 'location': location, 'offset': 0})

    '''
        @Author: @DeanLogan
        @Description: Parses the search result pages for job listings and handles pagination.
        @param: response - The response object containing the search result page data.
        @return: Yields requests for individual job pages and further search result pages.
    '''
    def parseSearchResults(self, response):
        # Callback for handling the search result pages
        location = response.meta['location']
        keyword = response.meta['keyword']
        offset = response.meta['offset']

        # Extract JSON data using regex from the page source
        scriptTag = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', response.text)

        if scriptTag is not None:
            # Parse JSON data
            jsonBlob = json.loads(scriptTag[0])

            # Paginate Through Jobs Pages
            if offset == 0:
                # Get total number of job results
                metaData = jsonBlob["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"]
                numResults = sum(category["jobCount"] for category in metaData)
                if numResults > 1000:
                    numResults = 50

                # Generate requests for pagination
                for offset in range(10, numResults + 10, 10):
                    url = self.getIndeedSearchUrl(keyword, location, offset)
                    yield scrapy.Request(url=url, callback=self.parseSearchResults, meta={'keyword': keyword, 'location': location, 'offset': offset})

            # Extract Jobs From Search Page
            jobsList = jsonBlob['metaData']['mosaicProviderJobCardsModel']['results']
            for index, job in enumerate(jobsList):
                if job.get('jobkey') is not None:
                    # Construct the URL for each job and yield request with 'parseJob' callback
                    jobUrl = 'https://www.indeed.com/m/basecamp/viewjob?viewtype=embedded&jk=' + job.get('jobkey')
                    yield scrapy.Request(url=jobUrl, 
                            callback=self.parseJob, 
                            meta={
                                'keyword': keyword, 
                                'location': location, 
                                'page': round(offset / 10) + 1 if offset > 0 else 1,
                                'position': index,
                                'jobKey': job.get('jobkey'),
                            })

    '''
        @Author: @DeanLogan
        @Description: Parses individual job pages, extracts job information, and yields the scraped data.
        @param: response - The response object containing the job page data.
        @return: Yields a dictionary with job-related information.
    '''
    def parseJob(self, response):
        # Callback for handling individual job pages
        location = response.meta['location']
        keyword = response.meta['keyword'] 
        page = response.meta['page'] 
        position = response.meta['position'] 

        # Extract JSON data using regex from the page source
        scriptTag = re.findall(r"_initialData=(\{.+?\});", response.text)

        if scriptTag is not None:
            # Parse JSON data
            jsonBlob = json.loads(scriptTag[0])
            job = jsonBlob["jobInfoWrapperModel"]["jobInfoModel"]

            # Yield scraped job information
            yield {
                'keyword': keyword,
                'location': location,
                'page': page,
                'position': position,
                'jobKey': response.meta['jobKey'],
                'jobTitle': job["jobInfoHeaderModel"]["jobTitle"],
                'companyName': job["jobInfoHeaderModel"]["companyName"],
                'jobDescription': job["sanitizedJobDescription"]
            }
