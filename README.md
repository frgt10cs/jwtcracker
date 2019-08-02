# JwtCracker

Script for bruteforcing weak JWT with dictionary

## Using

``./jwtcrackerDict.py [token] [dictionaryfile]``

### Example

``/jwtcrackerDict.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cDo4z86Y3pYdN6V0IejK7JPtlpTR5d4n3Ji2DcMf48k ../google-10000-english-master/google-10000-english-usa.txt
``

#### Output:

``words count:  10000``

``Checking |██████████████████████████████████████████████████| 100.0% Complete``

``Secret is: victory``
