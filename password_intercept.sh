#!/usr/bin/env bash
# example mitmdump --modify-body :~q:foo:@~/xss-exploit
# TV_USER user name as email address
# TV_PW password
# TV_DOMAIN domain
DUMMY_USER="dummy@dummy.com"
DUMMY_PW="dummy"

mitmdump --modify-body :~u "{$TV_DOMAIN}":userLoginId="{$DUMMY_USER}"&password="{$DUMMY_PW}"&rememberMe=true:userLoginId="{$TV_USER}"&password="{$TV_PW}"&rememberMe=true


