# HSE Libraries 

The _HSE Libraries_ are a collection of useful LabVIEW libraries developed over the years for and within our real-life projects. 
These libraries form the basis of all our applications, similar to a very basic framework.

This repository contains the following libraries:

* hse-application
  
  Bsic VIs and classes to manage the fundamental properties of an application like version, application paths and general infos.
  
* hse-configuration
  
  Classes for reading and writing configuration sources like .ini files.

* hse-db
  
  Database interfaces for various DB systems (eg Microsoft ADO and MySQL/MariaDB). An additional DQMH module, which capsules the DB interfaces, 
  can be used in DQMH projects.
  
* hse-dqmh

  This library contains helpers for loading and using DQMH modules. 
  It caters to the HSE-specific events and supports programmatic features of our 
  [Windows Application Template](https://gitlab.com/hampel-soft/dqmh/hse-application-template) applications.
  
* hse-gennet
  
  The _DQMH Generic Networking Module_ is a DQMH Singleton module altered to allow for (near) zero-coupled networking functionality.
  
* hse-misc
  
  This is a collection of useful VIs developed over the years for and within our real-life projects.
  
* hse-ui
  
  Useful helper VIs and tools for creating and manipulating user interfaces.
  

For a more detailed documentation please have a look at our DokuWiki https://dokuwiki.hampel-soft.com/code/open-source/hse-libraries.

## :question: FAQ
See our [FAQ](https://dokuwiki.hampel-soft.com/code/open-source/hse-libraries/20_faq) for comments on updating versions amongst other things.

## :rocket: Installation

> Don't go looking for a VI Package - there is none! If you're wondering why, read more about [how we work with reuse code at HSE](https://dokuwiki.hampel-soft.com/code/common/dependency-structure).

Just copy everything under the folder `Source` into your project structure and use it. You are free to remove any libs you don't want to 
use from the `Source` directory as long as this doesn't break the code!

The hse-libraries work best when used from a project based on the HSE [repository](https://dokuwiki.hampel-soft.com/code/common/repository-structure) 
and [project](https://dokuwiki.hampel-soft.com/code/common/project-structure) structure. 

The latest release version can be found at https://dokuwiki.hampel-soft.com/code/open-source/hse-libraries/releases.

### :wrench: LabVIEW 2020

The VIs are maintained in LabVIEW 2020.

### :link: Dependencies

These libraries depend on the HSE-Logger: https://dokuwiki.hampel-soft.com/code/open-source/hse-logger.


## :bulb: Usage

If you want to use the framework helpers (hse-application and hse-configuration), you can find more information about our file 
and project structure at https://dokuwiki.hampel-soft.com/code/common/project-structure.


## :busts_in_silhouette: Contributing 

We welcome every and any contribution. On our Dokuwiki, we compiled detailed information on 
[how to contribute](https://dokuwiki.hampel-soft.com/processes/collaboration). 
Please get in touch at (office@hampel-soft.com) for any questions.


##  :beers: Credits

* Joerg Hampel
* Manuel Sebald
* Alexander Elbert
* Francois Normandin (https://github.com/LabVIEW-Open-Source/DataManipulation)


## :page_facing_up: License 

This project is licensed under a modified BSD License - see the [LICENSE](LICENSE) file for details.
