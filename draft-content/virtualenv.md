Title: Virtual Environment Kurulumu
Date: 2012-02-26 11:20
Tags: python, virtualenv
Category: Tutorials
Slug: virtualenv-kurulumu
Author: ekinertac

Eğer python üzerinde geliştirme yapacaksanız, `virtualenv` yani Sanal Geliştirme Ortamı kurmanız çok çok faydanıza olacaktır. 
Virtualenv'i farklı python versiyonları, farklı paketler, kendi yazdığınız executable scriptler için kullanabilirsiniz.

Sisteminizde `easy_install, pip` gibi python paket manager'ları yüklümü değilmi kontrol edelim, eğer hiç biri yüklü değilse  kuruluma `setup-tools` ile başlayalım.

    $ easy_install
    $ pip

ikisinden birini terminalde çalıştırdığınızda 
    
    -bash: easy_install: command not found
    -bash: pip: command not found

satırlarından farklı çıktı alıyorsanız ikisinden birisi kuruludur. Eğer `easy_install` kurulu ise `pip` kurmamız şart.

    $ easy_install pip

sistemde `easy_install` dahi yüklü değilse `setup-tools` ile devam ediyoruz. [PyPi - SetupTools](https://pypi.python.org/pypi/setuptools#downloads) sayfasından yanında **Source** yazan linke tıklayıp son sürümü ediniyoruz.

    $ tar zxvf setuptools-0.6c11.tar.gz 
    $ cd setuptools-0.6c11
    $ python setup.py install

yazdıktan sonra setuptools kurulmuş durumda. Eğer `permission` hatası alırsanız `sudo python setup.py install` deneyerek kurulumu root olarak tamamlayabilirsiniz.

Setuptools kurulumu tamamlandıktan sonra:

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ virtualenv env_adi
Virtualenv yapısı için bir klasör yapısı geliştirmenizi öneririm yoksa işler sarpa sarıyor bir süre sonra.

    └── ~/Sites
        ├── proje_adi_1
        │   └── env_adi
        │   └── project
        │
        ├── proje_adi_2
        │   └── env_adi
        │   └── project
        │
        └── proje_adi_3
            └── env_adi
            └── project

Şeklinde oluşan bir yapı şimdiye kadar kullandığım en rahat ettiğim klasör yapısı.