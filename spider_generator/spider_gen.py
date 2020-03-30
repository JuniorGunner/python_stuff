# Spider Generator for Viva Real
import pandas as pd
import unidecode

def read_excel():
    df = pd.read_excel("Path/To/city_list.xlsx")
    df.drop_duplicates(inplace = True)
    cities = list(map(str.strip, df["CITY"].tolist()))

    return cities

def generator(cities):
    for city in cities:
        
        unaccent = "vivareal_" + unidecode.unidecode(city) # Remove word accent

        spider_name = unaccent.lower().replace(" ", "_") # Spider name pattern

        link_apto = """\n    start_urls = [ \"https://glue-api.vivareal.com/v1/listings?&filterUnitType=APARTMENT&addressCity={}&size=100&from=000\",\n""".format(city)
        link_home = "\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=HOME&addressCity={}&size=100&from=000\",\n".format(city)
        link_land = "\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=RESIDENTIAL_ALLOTMENT_LAND&addressCity={}&size=100&from=000\",\n".format(city)
        link_2story = "\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=TWO_STORY_HOUSE&addressCity={}&size=100&from=000\"]\n".format(city)

        base_file = open("Scrapy/Project/spiders/vivareal_city.py", "r")
        code_1 = base_file.read(1003)
        unused = base_file.read(709)
        code_2 = base_file.read(1938)

        new_spider = open("Scrapy/Project/spiders/{}.py".format(spider_name), "a")
        new_spider.write(code_1)
        new_spider.write(" \'" + spider_name + "\'")
        new_spider.write(link_apto)
        new_spider.write(link_home)
        new_spider.write(link_land)
        new_spider.write(link_2story)
        new_spider.write(code_2)

        new_spider.close()

if __name__ == "__main__":
    cities = read_excel()

    generator(cities)
