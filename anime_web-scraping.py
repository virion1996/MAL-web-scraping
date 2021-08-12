from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

""" pega as infos necessarias na pag de cada anime """
def get_anime_info(anime):
    href = anime.find_element(By.CLASS_NAME, "title").find_element(By.CLASS_NAME, "link").get_attribute("href")
    driver_anime.get(href)
    title_name = driver_anime.find_element_by_class_name("title-name").text
    score_label = driver_anime.find_element_by_class_name("score-label").text
    rank_num = driver_anime.find_element_by_class_name("ranked").text
    anime_obj = Anime(title_name, score_label, rank_num)
    return anime_obj
    
""" classe anime com as infos que gostaria de ter """
class Anime:
    def __init__(self, title_name, score, ranked):
        self.title_name = title_name
        self.score = score
        self.ranked = ranked

""" onde ta o chrome driver pra abrir o navegador """
PATH = "C:\Windows\chromedriver.exe"

""" url pra abrir """
url = "https://myanimelist.net/animelist/virion1996?status=1"

all_animes = []

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])

""" criando o driver pra fazer o web scraping """
driver = webdriver.Chrome(PATH, options = option)
driver_anime = webdriver.Chrome(PATH, options = option)

""" acessando o site """
driver.get(url)

""" pegando todos os elementos no site cuja classe = list-item 
    no site em questao, todos os animes listados estao dentro dessa classe"""
anime_list = driver.find_elements(By.CLASS_NAME, "list-item")


""" pega as infos de cada anime q apareceu na lista anterior
    e coloca o obj criado dentro da lista"""
for anime in anime_list:
    all_animes.append(get_anime_info(anime))

""" fecha os navegadores """
driver_anime.quit()
driver.quit()

""" sort atraves do score de cada anime em ordem decrescente """
all_animes.sort(reverse= True ,key = lambda a: a.score)

""" print """
for a in all_animes:
    print(a.title_name)


