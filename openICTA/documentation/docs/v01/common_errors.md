

** Can't find model 'en'
When receieving the follwing issue it might indicate that the English model is not present (in the right way) on the system `IOError: [E050] Can't find model 'en'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.`.

you can resolve this issue by manually execute the below command:
`python -m spacy download en`
