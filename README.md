# adidasOrderInfo

A simple adidas order information retriever.

Right now it just takes a screenshot, so you can tell what size it is, what step it's in, and the tracking number.

To be added:

* Parse HTML and put results in a file

# Installation & Setup

All you need to install is selenium system-wide and have python 3

```
pip install selenium
```

Fill your orders.csv file with the following format (sample in the repo)

<ordernum>,<email>
<ordernum2>,<email2>

# Running

```
python adiOrderTracker.py
```
