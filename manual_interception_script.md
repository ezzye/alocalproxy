# Manual Interception Script

`mitmproxy` operates on http://localhost:8080
Use `mitmproxy` to start command line `mitmproxy`
Set computer network to use proxy
Use `mitmdump -w outfile` to write all traffic to outfile
Analyse file and edit to replay command
Use `mitmdump -nC outfile` to replay outfile
Check results

Filter relevant password method
use `i` to set intercept
`~u ':userLoginId=<username>%40<emaildomain>&password=<password>&rememberMe=true&' & ~q`
Intercept and amend line

Output filtered line to outfile
URL `POST https://www.domain.com/gb/login HTTP/2.0`
CONTENT `userLoginId=<username>%40<emaildomain>&password=<password>&rememberMe=true&`
`mitmdump -w outfile ~u "www.domain.com/gb/login" & ~bq "userLoginId=first.last%40gmail.com&password=Pas123&rememberMe=true"`
Replay outfile login
`mitmdump -nC srcfile -w dstfile`



