#-------------------------------------------------------------------------------
# Name:        e-mail writer
#
# Author:      Léo
#
# Created:     05/04/2021
# Copyright:   (c) Léo fumet 2021
# All rights reserved
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:        e-mail writer
#
# Author:      Léo
#
# Created:     05/04/2021
# Copyright:   (c) Léo fumet 2021
# All rights reserved
#-------------------------------------------------------------------------------
lienid= "https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser"
n = 0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Idgoogle = ""
Mdpgoogle = ""
destinataire = ["destinataire@gmail.com", "destinataire@Waouh.org", "destinataire@ecosia.fr"]
objet = "objet du message"
corptexte = "corp du message"


driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get(lienid)
#connection ID
connectionid_search = driver.find_element_by_id("identifierId")
connectionid_search.send_keys(Idgoogle)
connectionid_val = driver.find_element_by_class_name("VfPpkd-RLmnJb")
connectionid_val.click()

#connection MDP
time.sleep(1)

connectionmdp_search = driver.find_element_by_class_name("zHQkBf")
connectionmdp_search.send_keys(Mdpgoogle)
connectionmdp_val = driver.find_element_by_class_name("VfPpkd-RLmnJb")
connectionmdp_val.click()

while n!= len(destinataire) :
    # séléctionner un message
    time.sleep(1)
    nouveaumessage_search = driver.find_element_by_class_name("z0")
    nouveaumessage_search.click()

    #écrire le message
    ecriredestinataire_search = driver.find_element_by_class_name("vO")
    ecriredestinataire_search.send_keys(destinataire[n])
    ecrireobjet_search = driver.find_element_by_class_name("aoT")
    ecrireobjet_search.send_keys(objet)
    ecriremessage_search = driver.find_element_by_class_name("gmail_signature")
    ecriremessage_search.click()
    ecriremessage_search.send_keys(Keys.ARROW_UP + corptexte)
    ecriremessage_search.send_keys(Keys.CONTROL + Keys.ENTER)
    n= n+1
