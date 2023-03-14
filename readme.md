## Exe build
```

pyinstaller --onefile --hidden-import='*' .\ec_main_v2.py -F --collect-all face_recognition_models
pyinstaller --onefile --hidden-import='*' .\nbr_tin_main.py                                         
pyinstaller --onefile --hidden-import='*' .\nbr_tax_main.py


```

## To Run the project

```

python .\ec_main_v2.py   
python .\nbr_tin_main.py
python .\nbr_tax_main.py




```

## Deployment dependency for ec_main

```
- Chrome driver if wdm is disabled (USE_WDM = 0 in common.env)
- Chrome browser
- VC_redist.x64
- odbc

```

## Required network access

```
- https://192.168.249.10/partner-portal/login
- https://verification.taxofficemanagement.gov.bd/
- https://secure.incometax.gov.bd/Registration/Login

```

## Change in nid.env

```
EC_NID_IMAGE_SAVING_LOCATION = 'media/ec_nid/test_photos/'
API_IMAGE_FOLDER_PATH = 'http://10.100.14.175:8111/media/'

```