from pytrends.request import TrendReq
import datetime
from dateutil.relativedelta import relativedelta
import time
import os
from urllib.parse import quote_plus
import logging
import itertools


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

# US CST https://pypi.org/project/pytrends/
pytrend = TrendReq(hl='en-US', tz=360) 

resolution = "DMA"

# combined -- keyword is a placeholder. will be replaced by combined keywords later.
directory2keywords = {
    "combined": ['fox news']
}

directory2period = {
    "combined": (datetime.date(2020,2,1), datetime.date(2020,5,10))   
}


try:
    os.mkdir("by_region")
except:
    pass


for keyword_for_directory in directory2keywords:
    logger.info("keyword_for_directory: {}".format(keyword_for_directory))
    keywords = directory2keywords[keyword_for_directory]
    keywords_indexes = list(range(0,len(keywords)))
    START_TIME, END_TIME = directory2period[keyword_for_directory]

    MAX_LENGTH = -1

    if not os.path.exists("by_region/" + keyword_for_directory):
        os.mkdir("by_region/" + keyword_for_directory)       

    for r in range(1,len(keywords)+1):
        for selected in list(itertools.combinations(keywords_indexes, r)):
            current_datetime = START_TIME            
            keyword = "+".join([keywords[i] for i in selected])
            if MAX_LENGTH != -1 and len(keyword) > MAX_LENGTH:
                logger.info("len(keyword)[{}] is longer than MAX_LENGTH[{}]".format(len(keyword), MAX_LENGTH))
                continue
            while True:
                if current_datetime > END_TIME:
                    break
                
                if os.path.exists("by_region/{}/{}-{}-{}-by_region.csv".format(keyword_for_directory,"_".join([str(s) for s in selected]), resolution, current_datetime.strftime("%Y%m%d"))):
                    logger.info("by_region/{}/{}-{}-{}-by_region.csv is collected...".format(keyword_for_directory,"_".join([str(s) for s in selected]), resolution, current_datetime.strftime("%Y%m%d"))) 
                    current_datetime += datetime.timedelta(days=1)   
                    continue

                try:
                    # combined
                    pytrend.build_payload(kw_list=['fox news', 'cdc', 'cnn'], geo="US", 
                                        timeframe='%s %s' % (current_datetime.strftime("%Y-%m-%d"), current_datetime.strftime("%Y-%m-%d"))) 
                    time.sleep(15)
                    df = pytrend.interest_by_region(resolution=resolution)
                    time.sleep(15)
                except:
                    logger.error("error", exc_info=1)
                    MAX_LENGTH = len(keyword)
                    time.sleep(120)


                df.to_csv("by_region/{}/{}-{}-{}-by_region.csv".format(keyword_for_directory,"_".join([str(s) for s in selected]), resolution, current_datetime.strftime("%Y%m%d")))
                current_datetime += datetime.timedelta(days=1)