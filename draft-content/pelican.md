Title: Pelican'a geçiş
Date: 2012-02-27 15:40
Tags: python, pelican
Category: Writings
Slug: pelican-a-gecis
Author: ekinertac

<meta property="og:image" content="http://www.php2s.com/wp-content/uploads/2012/06/python-logo-official.png"/>

Konuya direk giriş yapmadan önce hayatımıza yeni yeni girmiş olan **Static Blogging Engine** terimi üzerinde durmak lazım. Nedir bu **Static Blogging Engine** ? 

**Static Blogging Engine** kısa olarak yazdığınız [Markdown](http://daringfireball.net/projects/markdown/), [reStructuredText](http://docutils.sourceforge.net/rst.html) formatlı metin dosyalarınızı, muteşem bir şekilde static, yani herhangi bir server-side dile ihtiyaç duymadan yayınlayabileceğiniz html tabanlı bir bloga çeviren şahane yapıya deniyor.

İstediğiniz kadar caching yapın, dosya sıkıştırın html kadar hızlı render edilen bir yazılıma sahip olmak pekte mümkün bir olay değil. Siz yazıları **markdown** olarak yazıyorsunuz, blog engine'iniz size html yapısnı oluşturuyor. Tabi html diyince aklınıza sadece yazılardan oluşan sayfalar gelmesin, bunun içersinde bir blogda ihtiyaç duyulan neredeyse herşey mevcut. Tagler, kategoriler, comment sistemi, sosyal medya entegresi vs ne ararsanız çoğunlukla var.

Herşey o kadar basit düşünülmüş ki, ne bir admin paneliniz var ne başka bir yönetim sayfanız var. Herşey çok iyi bildiğiniz dosya sistemi üzerine kurulu.

<blockquote class="twitter-tweet" align="center" style="margin-bottom:20px"><p>I very much dislike the <a href="https://twitter.com/search/%23wordpress">#wordpress</a> editor … seriously considering moving everything to <a href="https://twitter.com/search/%23pelican">#pelican</a> <a href="http://t.co/IZeWLLR8" title="http://blog.notmyidea.org/pelican-a-simple-static-blog-generator-in-python.html">blog.notmyidea.org/pelican-a-simp…</a></p>&mdash; Andrew Lombardi (@kinabalu) <a href="https://twitter.com/kinabalu/status/273147147430543360">November 26, 2012</a></blockquote>
<script async src="http://platform.twitter.com/widgets.js" charset="utf-8"></script>

>

Bundan daha önce Wordpress başta olmak üzere Tumblr dan tutunda özene bezene CodeIgniter da yazdığım blog sistemlerine kadar çoğunu kullandım. Son olarak Django'ya çok fazla yöneldiğim için Django çatısı altında bir blog oluşturdum ama aklımın bir köşesinde hep bir **Static Blogging Engine** kullanarak bir blog yapma isteğim vardı. 


Peki kullanabileceğimiz Engine'ler hangileri ? 

- ####[Octopress](http://octopress.org/)
Octopress, [Brandon Mathis](http://brandonmathis.com/) tarafından tasarlanan [Jekyll](http://github.com/mojombo/jekyll) için hazırlanan, [Github Pages](http://pages.github.com/)'in arkasında da kullanılan bir statik blog framework'ü. En popüler engine olarak görülüyor ve gerçektende öyle.

Octopress'den sonra Ruby ile hazırlanmış [Webby](http://webby.rubyforge.org/), [StaticMatic](http://staticmatic.rubyforge.org/) ve [toto](http://cloudhead.io/toto) isimlerinde farklı blog engine'leride mevcut.

- ####[Pelican](http://docs.getpelican.com/en/latest/)
Pelican benimde kullandığım Python için yazılmış Octopress kadar başarılı bir blog framework'ü. Pelican'ı seçmemdeki tek amaç Python ekosistemine Ruby'e kıyasla çok daha alışkın olmam. Django/Jinja2 template taglerini desteklemeside ikinci büyük sebebim. Templateleri düzenlemek elim bu template diline alışkın olduğum için çok kolay oldu benim için.

    [Calepin](http://calepin.co/) ise Pelican için hazırlanmış, Dropbox üzerinde çalışan bir             blog **hosting** sistemi ve evet tahmin edebileceğiniz gibi tamamen **ücretsiz**. Calepin'in kullandığı fikir çok iyi bu arada, bahsetmeden geçemeyeceğim.

- ####Blosxom
- Blosxom için malesef link veremiyorum çünkü bu servis artık **[kapatılmış durumda](http://www.blosxom.com/)**. Static Blogging Engine sistemini geliştiren ilk servis olduğu için buraya eklemeyi uygun gördüm. Belki merak edip araştırmak isteyenler olabilir.

- ####[Second Crack](https://github.com/marcoarment/secondcrack)
Second Crack, PHP için hazırlanmış bir diğer statik blogging framework'ü.

- ####[Blacksmith](http://blog.nodejitsu.com/introducing-blacksmith)
Blacksmith ise Node.js'e daha yakın olanların kullanacağı 'cutting-edge' statik blog sistemlerinden en genci.

- Bunlar bana yetmez daha fazla blog engine istiyorum diyenleriniz varsa 32 adet blog engine'in anlatıldığı [Timo Reitnauer](https://twitter.com/treitnauer)'ın yazmış olduğu devasa yazıya [göz atabilirsiniz](https://iwantmyname.com/blog/2011/02/list-static-website-generators.html).


**Pelican** kullandığım için konuya bu statik framework üzerinden devam ediyorum. 

Pelican'ın kurulumu, tema seçimi ve yayına alması üzerinde editleme yapmayacaksaksanız bir kaç dakikanızı alabilir.

Kendimize bir terminal açıp hemen virtualenv'mizi oluşturmaya başlıyoruz. (sisteminizde virtualenv'nin kurulu olduğunu düşünüyorum, kurulu olmayanlar [buradan devam edebilirler](/virtualenv-kurulumu.html))
    
    $ mkdir pelican-blog
    $ cd peli*
    $ virtualenv env
    $ source env/bin/activate
    $ pip install pelican
<sub><sup>* işareti klavyedeki `tab` karateri için</sup></sub>

Pelican kurulumu bu kadar basit, ancak küçücük bir sıkıntımız var. Pelican'da Markdown desteği opsiyonel olarak geliyor o yüzden pelican kurulduktan sonrada Markdown kurmaya ihtiyacımız var.

    $ pip install Markdown
    
Markdown da virtualenv'mize kurulduktan sonra, Pelican için hemen bir yapı oluşturabiliyoruz

    $ pelican-quickstart
Bu komutu çalıştırdıktan sonra wizard bize birkaç soru soruyor

    Welcome to pelican-quickstart v3.1.1.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.

    
    > Where do you want to create your new web site? [.] project
    > What will be the title of this web site? Ekin Ertaç's WebBlog
    > Who will be the author of this web site? ekinertac
    > What will be the default language of this web site? [en] tr
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) Y
    > How many articles per page do you want? [10] 10
    > Do you want to generate a Makefile to easily manage your website? (Y/n) Y
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
    > Do you want to upload your website using FTP? (y/N) N
    > Do you want to upload your website using SSH? (y/N) N
    > Do you want to upload your website using Dropbox? (y/N) N
    Done. Your new project is available at /Users/ekinertac/Sites/test/project
    
Sorduğu sorular sırasıyla,

- Blog dosyalarını nerede tutmak istediğinizi soruyor, `project` yazarak bulunduğum klasörde `project` adında bir klasör oluşturup onun içine kurmasını istedim
- Blog başlığı ?
- Blog yazarı ?
- Web sitesinin dili ?
- Kullanacağınız domain ?
- Pagination kullanacakmısınız ?
- Sayfa başına kaç adet yazı olacağı ?
- Sayfanızı kolayca konfigüre edebilmek için Makefile oluşuturulsunmu ?
- templateler için veya yazı yazarken live olarak değişiklikleri görebilmeniz için Pelicanın sunduğu script desteği ?
- FTP desteği ?
- SSH desteği ?
- Dropbox desteği ?

Bu sorulara cevap verdikten sonra blogumuz neredeyse hazır durumda.

`project/content` klasörünün içine girip ilk yazınızı yazmaya başlayabilirsiniz. Klasörün içinde `first-post.md` adlı bir dosya oluşturuyorum ve dosyanın içine **herhangi** bir text editöründe

    Title: Pelican'a geçiş
    Date: 2012-02-27 15:40
    Tags: python, pelican
    Category: Writings
    Slug: pelican-a-gecis
    Author: ekinertac

satırlarını ekliyorum. Bu satırlar görüldüğü gibi blog post'unun meta bilgilerini saklıyor.
İki alt satıra geçerek yazmaya başlıyorum.

    Title: Pelican'a geçiş
    Date: 2012-02-27 15:40
    Tags: python, pelican
    Category: Writings
    Slug: pelican-a-gecis
    Author: ekinertac

    Konuya direk giriş yapmadan önce hayatımıza yeni yeni girmiş olan **Static Blogging Engine** terimi üzerinde durmak lazım. Nedir bu **Static Blogging Engine** ? 
    
hemen ardından hızlı bir test için terminale geri dönüp

    $ make html
    
komutunu çalıştırıyorum, ve herhangi bir hata yoksa, `project/output` klasörü altında .html dosyalarım **yayınlanmaya hazır** olarak bekliyor.

Daha fazla dökümantasyon için Pelican'ın **bol detaylı** [dökümantasyon](http://docs.getpelican.com/en/latest/getting_started.html) sayfasını ziyaret edebilirsiniz.
