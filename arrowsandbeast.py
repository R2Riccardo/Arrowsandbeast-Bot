# ------------------------------------------------------------------------------- #

import logging
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from termcolor import colored
from colorama import Fore, init
from dhooks import Webhook, Embed
from termcolor import colored

# ------------------------------------------------------------------------------- #

with open('config.json') as f:
    config = json.load(f)

webhook = config['settings']['webhook']
firstname = config['settings']['firstname']
lastname = config['settings']['lastname']
email = config['settings']['email']
street1 = config['settings']['street1']
street2 = config['settings']['street2']
city = config['settings']['city']
zipcode = config['settings']['zipcode']
country = config['settings']['country']
state = config['settings']['state']
phone = config['settings']['phone']

print(colored('    _________                    _____       __      __  _                 ', 'magenta', attrs=['bold']))
print(colored('   / ____/ (_)  ____  _______   / ___/____  / /_  __/ /_(_)___  ____  _____', 'magenta', attrs=['bold']))
print(colored('  / __/ / / / |/_/ / / / ___/   \__ \/ __ \/ / / / / __/ / __ \/ __ \/ ___/', 'magenta', attrs=['bold']))
print(colored(' / /___/ / />  </ /_/ / /      ___/ / /_/ / / /_/ / /_/ / /_/ / / / (__  ) ', 'magenta', attrs=['bold']))
print(colored('/_____/_/_/_/|_|\__, /_/      /____/\____/_/\__,_/\__/_/\____/_/ /_/____/  ', 'magenta', attrs=['bold']))
print(colored('               /____/                                                         Developer Version', 'magenta', attrs=['bold']))
print('')


link=input("Link: ")

# ------------------------------------------------------------------------------- #

def create_arrowsBOT():

    # ------------------------------------------------------------------------------- #

    options=webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"')
    
    # ------------------------------------------------------------------------------- #

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', service_log_path='./debug.log', options=options)
    driver.get("" + link + "")
    print("Succesfully opened Arrow and Beast Website.")
    sleep(1)
    driver.find_element_by_xpath("/html/body/section[1]/section[3]/div/div[3]/section/div/div[2]/div/form/div[3]/div[3]/div[1]/div/div/div/dd/div/ul/li[1]").click()
    print("Succesfully found Size.")
    sleep(1)
    driver.find_element_by_xpath("/html/body/section[1]/section[3]/div/div[3]/section/div/div[2]/div/form/div[3]/div[3]/div[2]/div[2]/div[2]/button").click()
    print("Succesfully Added to Cart.")
    sleep(1)
    driver.get("https://www.arrowandbeast.com/checkout/onepage/?___SID=S")
    sleep(0)
    print("Submitting Shipping Infos.")
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[1]/div[2]/div/div[1]/div[1]/ul/li[1]/input").click()
    sleep(0)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[1]/div[2]/div/div[1]/div[1]/ul/li[1]/input").click()
    sleep(0)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[1]/div[2]/div/div[1]/div[2]/button").click()
    fill_out_firstname=driver.find_element_by_name("billing[firstname]")
    fill_out_firstname.send_keys(firstname)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[1]/div/div[2]/div/input").click()    
    fill_out_lastname=driver.find_element_by_name("billing[lastname]")
    fill_out_lastname.send_keys(lastname)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[2]/div[2]/div/input").click()    
    fill_out_email=driver.find_element_by_name("billing[email]")
    fill_out_email.send_keys(email)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[3]/div/input").click()    
    fill_out_street1=driver.find_element_by_name("billing[street][]")
    fill_out_street1.send_keys(street1)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[4]/div/input").click()    
    fill_out_street2=driver.find_element_by_name("billing[street][]")
    fill_out_street2.send_keys(street2)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[5]/div[1]/div/input").click()    
    fill_out_city=driver.find_element_by_name("billing[city]")
    fill_out_city.send_keys(city)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[6]/div[2]/div/select").click()    
    fill_out_country=driver.find_element_by_name("billing[country_id]")
    fill_out_country.send_keys(country)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[6]/div[1]/div/input").click()    
    fill_out_zipcode=driver.find_element_by_name("billing[postcode]")
    fill_out_zipcode.send_keys(zipcode)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/ul/li[1]/fieldset/ul/li[7]/div/div/input").click()    
    fill_out_phone=driver.find_element_by_name("billing[telephone]")
    fill_out_phone.send_keys(phone)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[2]/div[2]/form/fieldset/div/div/button").click()
    sleep(6)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[4]/div[2]/form/div[3]/div/button").click()
    print("Submitting Shipping Method.")
    sleep(5)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[5]/div[2]/form/fieldset/dl/dt[1]/input").click()
    print("Succesfully selected Bank Transfer.")
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[5]/div[2]/div[2]/div/button").click()
    sleep(5)
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[6]/div[2]/div/form/ol/li[1]/p/input").click()
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[6]/div[2]/div/form/ol/li[2]/p/input").click()
    driver.find_element_by_xpath("/html/body/section/section[3]/div/div/section/div/ol/li[6]/div[2]/div/div[2]/div/div/button").click()
    print("Succesfully submitted order, check your inbox.")

    hook = Webhook(url=webhook)

    embed = Embed(
        color=0xFF00FF,
        timestamp=True
    )

    embed.set_author(name='Arrows and Beast ACO')
    embed.add_field(name='Product', value=link, inline=False)
    embed.add_field(name='Size', value=f'US 8', inline=False)
    embed.add_field(name='Payment Method', value=f'Bank Transfer', inline=False)
    embed.add_field(name='Profile', value="||Riccardo||", inline=False)
    embed.set_footer(text="Elixyr Solutions", icon_url='https://cdn.discordapp.com/attachments/703310112193773578/703316503784849478/ElixyrLogo.png')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/738498975514230824/740579274456694884/download.png")

    hook.send(embeds=embed)
    sleep(20)
    quit()

    # ------------------------------------------------------------------------------- #
    
create_arrowsBOT()