{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "from splinter import Browser\n",
    "from splinter.exceptions import ElementDoesNotExist\n",
    "import os\n",
    "import pymongo\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scrape with Splinter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup = bs(browser.html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Examine the results, then determine element that contains sought info\n",
    "# print(browser.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve all elements that contain book information\n",
    "# articles = soup.find_all('div', class_='content_title')\n",
    "article = soup.find('li', class_='slide')\n",
    "# article_section = soup.find_all('li')\n",
    "# article_section.contents.find_all('li')\n",
    "# print(article)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA Readies Perseverance Mars Rover's Earthly Twin \n",
      "Did you know NASA's next Mars rover has a nearly identical sibling on Earth for testing? Even better, it's about to roll for the first time through a replica Martian landscape.\n"
     ]
    }
   ],
   "source": [
    "article_title_tag = article.find('div', class_='content_title')\n",
    "article_contents = article.find('div', class_='article_teaser_body')\n",
    "news_title = article_title_tag.text\n",
    "news_p = article_contents.text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "home_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(home_url)\n",
    "# print(browser.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\cmira\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:493: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  FutureWarning,\n"
     ]
    }
   ],
   "source": [
    "browser.click_link_by_partial_text('FULL IMAGE')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/spaceimages/images/mediumsize/PIA18897_ip.jpg\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "# print(html)\n",
    "img_tag = soup.find('img', class_='fancybox-image')\n",
    "print(img_tag['src'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18897_ip.jpg\n"
     ]
    }
   ],
   "source": [
    "featured_image_url = 'https://www.jpl.nasa.gov' + img_tag['src']\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scrape with Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>0</th>\\n      <th>1</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Equatorial Diameter:</td>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Polar Diameter:</td>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Orbit Distance:</td>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Orbit Period:</td>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Surface Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>7</th>\\n      <td>First Record:</td>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>8</th>\\n      <td>Recorded By:</td>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_table = df.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save to file\n",
    "df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "# print(browser.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/cerberus_enhanced\"><img alt=\"Cerberus Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/cerberus_enhanced\"><h3>Cerberus Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…</p></div> <!-- end description --></div>, <div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/schiaparelli_enhanced\"><img alt=\"Schiaparelli Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/schiaparelli_enhanced\"><h3>Schiaparelli Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…</p></div> <!-- end description --></div>, <div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/syrtis_major_enhanced\"><img alt=\"Syrtis Major Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/syrtis_major_enhanced\"><h3>Syrtis Major Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…</p></div> <!-- end description --></div>, <div class=\"item\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/valles_marineris_enhanced\"><img alt=\"Valles Marineris Hemisphere Enhanced thumbnail\" class=\"thumb\" src=\"/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png\"/></a><div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/valles_marineris_enhanced\"><h3>Valles Marineris Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…</p></div> <!-- end description --></div>]\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "# print(html)\n",
    "img_items = soup.find_all('div', class_='item')\n",
    "# print(img_items)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Cerberus Hemisphere Enhanced', 'img_url': '/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': '/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': '/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': '/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png'}]\n"
     ]
    }
   ],
   "source": [
    "for img_item in img_items:\n",
    "    # print('page:', img_item)\n",
    "    # print('-------------------------------------------------------------------------------------------------------')\n",
    "    title = img_item.find('h3')\n",
    "    img_tag = img_item.find('img')\n",
    "    link = img_tag['src']\n",
    "    # print(title)\n",
    "#    print(\"Title: \" + title.text)\n",
    "#    print(\"Link: \" + link)\n",
    "#    print('-------------------------------------------------------------------------------------------------------')\n",
    "    hemisphere_image_urls.append({'title': title.text, 'img_url': link})\n",
    "print(hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
