# ----------------------------------------------------------------------------
# name : nlpLogic.py
#
#
# short discription:
# nlpLogic forms the backbone for calling all NLP based operations on the text
# provided to the openICTA. This will be primary focus (at this moment in time)
# on providing a simplied binding towards spaCy for handling more complex 
# operations and suport in returning less complex answers to the main code. As
# from that point of view nlpLogic is more a binding solution between openICTA
# and spaCy.
#
#
# change log:
# DATE         DEVELOPER                     REASON
# 08JUN18      johan.louwers@capgemini.com   initial release to github
# 08JUN18      johan.louwers@capgemini.com   creating a number of placeholders
#                                            in the form of empty functions to
#                                            ensure future development on them
# 08JUN18      johan.lowuers@capgemini.com   release to github
#
# ----------------------------------------------------------------------------


# import all needed libs 
import spacy
from spacy_cld import LanguageDetector
#import en_core_web_sm
from spacy.lang.en import English

# function languageList
# function languageList will return all languages available within the solution
# this is more of a helper function and can potentially be used for building a
# gui solution at a later moment in time. Code should get the lLanguageList
# values in a more dynamic (config) based manner and should not rely on the 
# hardcoded values as done in the initial release.   
def languageList():
  lLanguageList = ['NL','US','DE']
  print '[%s]' % ', '.join(map(str, lLanguageList))
  return;




# function languageDetect
# function languageDetect is used to detect the language of the provided string
# to ensure you can select the correct langauge options for additional NLP based
# operations. It is possible to inlcude language detection in your logic directly
# or you can make sure you us languageDetect first and provide the outcome as 
# input directly to another logic function within the code. 
def languageDetect( basetext ):
  if type(basetext) != str:
    print "ERROR; the value is not a string" 
  else:
    nlp = spacy.load('en')
    # language_detector = LanguageDetector()
    # nlp.add_pipe(language_detector)
    # doc = nlp('This is some English text.')

    print (basetext)

  return;

languageDetect("abc");
languageList();


