from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PropertiesReader import PropertiesReader
from Logger import Logger
import time
import random

class InstagramBot:

    __logger = Logger()

    def __init__(self, geckoDriver, paginaInicial, paginaTags, paginaFoto,
        username, password, totalLikes, profileUrl, executaCurtir, hashTag):
        self.__geckoDriver = geckoDriver
        self.__paginaInicial = paginaInicial
        self.__paginaTags = paginaTags   
        self.__paginaFoto = paginaFoto
        self.__username = username
        self.__password = password
        self.__driver = webdriver.Chrome(
            executable_path=self.__geckoDriver
        )
        self.__totalLikes = totalLikes
        self.__profileUrl = profileUrl
        self.__executaCurtir = executaCurtir
        self.__hashTag = hashTag

    def __login(self):
        driver = self.__driver
        driver.get(self.__paginaInicial)
        time.sleep(random.randint(2, 4))

        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            pass

        # Preenche usuário
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.__username)
        time.sleep(random.randint(4, 6))

        # Preenche senha
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.__password)
        time.sleep(random.randint(4, 6))

        # Clica no botão
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))

    #@staticmethod
    #def __type_like_a_person(sentence, single_input_field):
    #    """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
    #    print("going to start typing message into message share text area")
    #    for letter in sentence:
    #        single_input_field.send_keys(letter)
    #        time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hastag(self):
        # Efetua login na página
        self.__login()

        # Abre a página da hashtag escolhida
        driver = self.__driver
        driver.get(self.__paginaTags + self.__hashTag + "/")
        driver.switch_to.window(driver.window_handles[0]) # Atribui um handler para controle de janela
        time.sleep(random.randint(5, 7))

        __pageBottomFound = False
        __saidaInformada = False
        __contaLikes = 0
        __contaFotos = 0
        __pic_rec = {'href': '', 'analisado': False}
        __pic_hrefs = [__pic_rec]
        while (not __pageBottomFound):

            # Rola a página para carregar mais fotos
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(7, 11))

            # Checa se o final da página foi atingido
            __pageBottomFound = driver.execute_script("if ((window.innerHeight + window.scrollY) >= document.body.scrollHeight) "+
                "{ return true; } else { return false; }")
            
            # Captura todas as imagens da página
            __hrefs = driver.find_elements_by_tag_name("a")
            __genpic_hrefs = [elem.get_attribute("href") for elem in __hrefs]

            # Verifica se as fotos já foram analisadas
            for __genpic_href in __genpic_hrefs:
                __found = False
                for __pic in __pic_hrefs:
                    if (__pic['href'] == __genpic_href):
                        __found = True
                if (not __found) and (__genpic_href.find(self.__paginaFoto + "/") != -1):
                    __pic_rec['href'] = __genpic_href
                    __pic_rec['analisado'] = False
                    __pic_hrefs += [__pic_rec]       

            # Remove as imagens genéricas e deixa somente as fotos a serem curtidas
            for __pic in __pic_hrefs: 
                if (not __pic['analisado']):

                    # Abre uma nova aba e carrega a página da foto
                    time.sleep(random.randint(5, 8))
                    driver.execute_script("window.open('"+__pic['href']+"','new window')")
                    driver.switch_to.window(driver.window_handles[1]) # Atribui um handler para controle de janela

                    try:

                        # Conta o total de fotos analisadas
                        __contaFotos += 1

                        # Verifica se a foto já foi curtida ou não
                        buttons = driver.find_elements_by_xpath('//button[@class="wpO6b "]')
                        for button in buttons:
                            if button.get_attribute('innerHTML').find('aria-label="Curtir"') != -1:
                                __contaLikes += 1
                                if self.__executaCurtir == "true":
                                    button.click()
                                    self.__logger.log(str(__contaLikes) + " curtida(s): " + __pic['href'] + ". " 
                                        + str(__contaFotos) + ' analisada(s)')
                                else:    
                                    self.__logger.log(str(__contaLikes) + " curtida(s) simulada(s): " + __pic['href'] + ". " 
                                        + str(__contaFotos) + ' analisada(s)')
                                __pic['analisado'] = True     
                                break
                            elif button.get_attribute('innerHTML').find('aria-label="Descurtir"') != -1:
                                self.__logger.log('Ja curtida: ' + __pic['href'] + ". " 
                                    + str(__contaLikes) + ' curtida(s). '
                                    + str(__contaFotos) + ' analisada(s)')
                                __pic['analisado'] = True    
                                break
                            else:
                                self.__logger.log('Botões nao encontrados: ' + __pic['href'] + ". " 
                                    + str(__contaLikes) + ' curtida(s). '
                                    + str(__contaFotos) + ' analisada(s)')
                                break

                        time.sleep(random.randint(15, 19))

                        # Fecha a aba
                        driver.execute_script("window.close()")

                        # Retorna o controle para a janela principal
                        driver.switch_to.window(driver.window_handles[0])

                        if (__contaLikes >= self.__totalLikes):
                            if (not __saidaInformada):
                                self.__logger.log("Atingido o limite de likes informado: " + str(__contaLikes))
                            __saidaInformada = True
                            break

                    except Exception as e:
                        self.__logger.log(e)
                        time.sleep(random.randint(5, 7))     

            if (__contaLikes >= self.__totalLikes):
                if (not __saidaInformada):
                    self.__logger.log("Atingido o limite informado de curtidas: " + str(__contaLikes))
                __saidaInformada = True
                break
            elif (__pageBottomFound):
                if (not __saidaInformada):
                    self.__logger.log("Atingido o final da página")
                __saidaInformada = True
                break

        self.__logger.log(
            "Hashtag: " + self.__hashTag + ". " +
            "Total de fotos analisadas: " + str(__contaFotos) + ". "
            "Total de likes: " + str(__contaLikes) + "."
            )

        self.__logoff() 

    def __logoff(self):
        driver = self.__driver
        driver.get(self.__profileUrl)
        time.sleep(random.randint(5, 7))

        # Clica no botão opções
        buttons = driver.find_elements_by_xpath('//button[@class="wpO6b "]')
        for button in buttons:
            if button.get_attribute('innerHTML').find('aria-label="Opções"') != -1: 
                button.click()
                time.sleep(random.randint(2, 4))
                break

        # Clica no menu Sair
        buttons = driver.find_elements_by_xpath('//button[@class="aOOlW   HoLwm "]')
        for button in buttons:
            if button.get_attribute('innerHTML').find('Sair') != -1: 
                button.click()
                break

        # Fecha o browser
        time.sleep(random.randint(5, 10))
        driver.quit

myReader = PropertiesReader()

myBot = InstagramBot(
    myReader.geckoDriver          # Driver de browser do Selenium
    , myReader.paginaInicial      # Página inicial do Instagram
    , myReader.paginaTags         # Página de tags (Hashtag)
    , myReader.paginaFoto         # Página de fotos para curtidas
    , myReader.usuario            # Usuário
    , myReader.senha              # Senha
    , myReader.totalLikes         # Total de likes
    , myReader.paginaPerfil       # Página do perfil
    , myReader.executaCurtir      # Decide se executa ou não o click do curtir
    , myReader.hashTag            # Hashtag a ser pesquisada
)

myBot.curtir_fotos_com_a_hastag()