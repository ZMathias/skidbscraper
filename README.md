## A scrapy project with spiders written to extract ski resort data from [skiresort.info](https://www.skiresort.info/).
Here is how to create a json dump featuring links to every European ski-resort available on the website:

    
    cd skidbscraper
    scrapy crawl skiresort -O resort-links.json

- The ski-resort spider creates a json array of links to the ski-resorts. For convenience, there is a script included to convert the json array to
  a plain-text file where the links are placed each in a new line


**To extract the data from the website of a ski-resort, run:**

    scrapy crawl resort -O resort-data.json
- This creates an array of JSON objects with the following structure:

      [
          {
              'name': name,
              'rating': rating
              'country': country,
              'county': county,
              'elevation': elevation,
              'slope_lengths': {
                  'total': total_slope_length,
                  'blue': blue_slope_length,
                  'red': red_slope_length,
                  'black': black_slope_length,
                  'additional': additional_slope_length
              },
      
              'pass_prices': {
                  'adult': adult_pass_price,
                  'youth': youth_pass_price,
                  'child': child_pass_price,
              },
      
              'season_start': season_interval[0].strip(),
              'season_end': season_interval[1].strip(),
              'opening_time': open_hours[0].strip(),
              'closing_time': open_hours[1].strip(),
              'neighbouring_towns': neighbouring_towns
          },
          
          ...
      ]
