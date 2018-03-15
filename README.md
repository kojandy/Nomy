# Nomy
Website Update Checker

## Install
```sh
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
Use with `crontab` for repetitive checks

## Settings
### Sample `settings.yml`
```yaml
notify:
    url: https://api.telegram.org/bot(deleted):(deleted)/sendMessage?chat_id=(deleted)&text={msg}
    message:
        registered: Registered! {name}
        updated: Updated! {name} {url}

check:
    - name: ProbProg
      url: https://raw.githubusercontent.com/hongseok-yang/probprog18/master/README.md
      xpath: //body
    - name: Graphics
      url: http://vclab.kaist.ac.kr/cs380/
      xpath: (//table[@style="font-size:14px; margin:0; padding:0;color:#666666;"])[1]
    - name: HCI
      url: https://kixlab.org/courses/cs374-spring-2018/
      xpath: (//div[@class="col-md-12"])[2]
```
