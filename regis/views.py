from django.shortcuts import render

# Create your views here.
def zealid_find(request, zeal_id):
	q = reg_table.objects.get(zealid = zeal_id)
	new_reg_table.objects.create(q)
	