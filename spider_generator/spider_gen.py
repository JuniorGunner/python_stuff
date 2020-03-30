# Spider Generator for Viva Real
import pandas as pd
import unidecode

def read_excel():
    df = pd.read_excel("Path/To/city_list.xlsx")
    cities = list(map(str.strip, df["CITY"].tolist())) # Creates a city list from DataFrame

    return cities

def generator(cities):
    for city in cities:
        
        unaccent = unidecode.unidecode(city) # Remove word accent

        spider_name = unaccent.lower().replace(" ", "_") # spider

        link_apto = """ start_urls = [
                    \t\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=APARTMENT&addressCity={}&size=100&from=000\",\n""".format(city)
        link_home = "\t\t\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=HOME&addressCity={}&size=100&from=000\",\n".format(city)
        link_land = "\t\t\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=RESIDENTIAL_ALLOTMENT_LAND&addressCity={}&size=100&from=000\",\n".format(city)
        link_2story = "\t\t\"https://glue-api.vivareal.com/v1/listings?&filterUnitType=TWO_STORY_HOUSE&addressCity={}&size=100&from=000\"]\n".format(city)

        base_file = open("Scrapy/Project/Spiders//vivareal_my_city.py", "r")
        code_1 = base_file.read(1003)
        unused = base_file.read(709)
        code_2 = base_file.read(1938)
        # print("\nUnused:\n\n", unused)
        # print("\nCode 2:\n\n", code_2)

        new_spider = open("Scrapy/Project/Spiders/vivareal_{}.py".format(spider_name), "a")
        new_spider.write(code_1)
        new_spider.write(link_apto)
        new_spider.write(link_home)
        new_spider.write(link_land)
        new_spider.write(link_2story)
        new_spider.write(code_2)

        new_spider.close()
        break

if __name__ == "__main__":
    cities = read_excel()
    # print(cities)
    generator(cities)
