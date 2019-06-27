# textclassifier
A light weight supervised text classifier written in Python!  This supervised classifier can take your simple training set and return a best category for the input text.

## Training file format

Place a training.txt file in the current folder and the format is as follows,

```
__label__category1 training data
__label__category1 some other data
__label__category2 some data
```

Text followed by __label__ is the category name, followed by a space then the input sentence.

## Invoking the classifier

```python
import classifier
results = classifier.classify("offer linkedin linkedin", "somerandomcategory")
```
`results` will be a list of tuple, like [('category'1', 10), ('category2',5)] sorted by top match first. 10,5 are the scores i.e number of word matches. "somerandomcategory" is the default category that you will receive in the event of no match!

If you need more powerful/accurate classification and you have a huge training set, refer my blog article for other options!
