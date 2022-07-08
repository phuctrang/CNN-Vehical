import os
import requests 
from bs4 import BeautifulSoup

Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# needed for google search
u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} #write: 'my user agent' in browser to get your browser user agent details

Image_Folder = 'bus'
Image_Folder1 = 'car'
Image_Folder2 = 'motobike'

def main():
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images_bus()
    if not os.path.exists(Image_Folder1):
        os.mkdir(Image_Folder1)
    download_images_car()
    if not os.path.exists(Image_Folder2):
        os.mkdir(Image_Folder2)
    download_images_motobike()

def download_images_bus():
    for i in range(0,5):
        if i ==0: 
            # Từ khóa search là 'bus'
            data = 'bus'
            num_images = 80
            # print('Searching Images bus....') 
            search_url = Google_Image + 'q=' + data #'q=' because its a query
            # request url, without u_agnt the permission gets denied
            response = requests.get(search_url, headers=u_agnt)
            html = response.text #To get actual result i.e. to read the html data in text mode
            # find all img where class='rg_i Q4LuWd'
            b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
            results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
            #extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
            #allow to continue the loop in case query fails for non-data-src attributes
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break      
                except KeyError:
                    continue
            print(f'Found {len(imagelinks)} images')
            print('Start downloading...')
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)            
                imagename = Image_Folder + '/' + data + str(j+1) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 1:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                
                imagename = Image_Folder + '/' + data + str(j+81) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 2:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)      
                imagename = Image_Folder + '/' + data + str(j+161) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 3:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                imagename = Image_Folder + '/' + data + str(j+241) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 4:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                imagename = Image_Folder + '/' + data + str(j+321) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
            break

def download_images_car():
    for i in range(0,5):
        if i ==0: 
            # Từ khóa search là 'car'
            data = 'car'
            num_images = 80
            print('Searching Images car....')
            search_url = Google_Image + 'q=' + data #'q=' because its a query
            # request url, without u_agnt the permission gets denied
            response = requests.get(search_url, headers=u_agnt)
            html = response.text #To get actual result i.e. to read the html data in text mode
            # find all img where class='rg_i Q4LuWd'
            b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
            results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
            #extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
            #allow to continue the loop in case query fails for non-data-src attributes
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break    
                except KeyError:
                    continue
            print(f'Found {len(imagelinks)} images')
            print('Start downloading...')
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)     
                imagename = Image_Folder1 + '/' + data + str(j+1) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 1:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                imagename = Image_Folder1 + '/' + data + str(j+81) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 2:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)   
                imagename = Image_Folder1 + '/' + data + str(j+161) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
            # break
        elif i == 3:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                
                imagename = Image_Folder1 + '/' + data + str(j+241) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 4:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)  
                imagename = Image_Folder1 + '/' + data + str(j+321) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
            break

def download_images_motobike():
    for i in range(0,5):
        if i ==0: 
            # Từ khóa search là 'motobike'
            data = 'motobike'
            num_images = 80
            print('Searching Images moto....')
            search_url = Google_Image + 'q=' + data #'q=' because its a query
            # request url, without u_agnt the permission gets denied
            response = requests.get(search_url, headers=u_agnt)
            html = response.text #To get actual result i.e. to read the html data in text mode
            # find all img where class='rg_i Q4LuWd'
            b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
            results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
            #extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
            #allow to continue the loop in case query fails for non-data-src attributes
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break 
                except KeyError:
                    continue
            print(f'Found {len(imagelinks)} images')
            print('Start downloading...')
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                imagename = Image_Folder2 + '/' + data + str(j+1) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 1:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                
                imagename = Image_Folder2 + '/' + data + str(j+81) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 2:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                
                imagename = Image_Folder2 + '/' + data + str(j+161) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
            # break
        elif i == 3:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)   
                imagename = Image_Folder2 + '/' + data + str(j+241) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
        elif i == 4:
            count = 0
            imagelinks= []
            for res in results:
                try:
                    link = res['data-src']
                    imagelinks.append(link)
                    count = count + 1
                    if (count >= num_images):
                        break
                except KeyError:
                    continue
            for j, imagelink in enumerate(imagelinks):
                # open each image link and save the file
                response = requests.get(imagelink)
                
                imagename = Image_Folder2 + '/' + data + str(j+321) + '.jpg'
                with open(imagename, 'wb') as file:
                    file.write(response.content)
            print('Download Completed!')
            break

if __name__ == '__main__':
    main()
