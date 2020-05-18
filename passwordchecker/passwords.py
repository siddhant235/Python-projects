import requests
import hashlib
import sys
def request_api(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching:{res.status_code}')
    return res
def leaked(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0;
def pwned_api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
   # return sha1password
    first,tail=sha1password[:5],sha1password[5:]
    response=request_api(first)
    return leaked(response,tail)
def main(args):
    for passwords in args:
        count=pwned_api_check(passwords)
        if count:
            print(f'{passwords} was found {count} times .. you should change it')
        else:
            print(f'{passwords} was notfound cary on')
if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))
