#!rm -f wdp_cos.py*
#!wget https://raw.githubusercontent.com/raanonr/DSX/master/Notebooks/wdp_cos.py
#!wget https://raw.githubusercontent.com/raanonr/DSX/a1f8a7876cf9ba115a2a14b784c48c566549fd2a/Notebooks/wdp_cos.py

import wdp_cos

cos = wdp_cos.get_cos("2SozF9MkHGQULJZHZTiZOnidaLSc3zIqr3SkDUC0YD0t", "crn:v1:bluemix:public:cloud-object-storage:global:a/db0d062d2b4c0836e18618a5222d8068:22e3b946-6154-4032-8e8f-7cfb0b429602::")

wdp_cos.list_buckets(cos)
