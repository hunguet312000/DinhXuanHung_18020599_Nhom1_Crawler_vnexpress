import scrapy

class Vnexpress(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ['vnexpress.net']
    start_urls = ["https://vnexpress.net/"]
    count = 0

    def parse(self, response):
        if response.status == 200 and response.css('meta[name="tt_page_type"]::attr("content")').get() == 'article':
            f = open('D:/PyCharm/CodePythyon/Vnexpress/Vnexpress.txt', 'a', encoding='utf8')

            Link = response.url
            f.write('[Bài viết] ' + Link.strip() + '\n')
            f.write('\n')

            for i in response.css('ul.breadcrumb li'):
                category = i.css('a::attr("title")').get()
                f.write(str(category).strip() + ' || ')
            f.write('\n')
            f.write('\n')

            Date = response.css('span.date::text').get()
            f.write(str(Date).strip() + '\n')
            f.write('\n')

            Title = response.css('h1.title-detail::text').get()
            f.write(str(Title).strip() + '\n')
            f.write('\n')

            SubTitle = response.css('p.description::text').get()
            f.write(str(SubTitle).strip() + '\n')
            f.write('\n')

            for i in response.css('article.fck_detail p.Normal'):
                content = ''.join(i.css('*::text').getall())
                f.write(content.strip() + '\n')

            f.write('Tags:')
            Tags = response.css('meta[name = "its_tag"]::attr("content")').getall()
            f.write(str(Tags).strip() + '\n')
            f.write('\n')

            self.count += 1
            self.crawler.stats.set_value('CRAWL COUNT', self.count)

        yield from response.follow_all(css='a[href^="https://vnexpress.net/"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)









