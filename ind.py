from bottle import route, run, template, get, post, put, delete, request
patient_dict={}
patient_info=[]

@post('/patient') 
def add_patient():   
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    patient_info = ' '.join([p_name,p_gender,p_age,p_address,p_phone])
    patient_dict.update({p_id:patient_info})
    return patient_dict

@get('/patient/<p_id>')
def show_patient(p_id):
    return patient_dict

@put('/patient/<p_id>')
def update_info(p_id):
	if p_id in patient_dict.keys():
		p_id = request.POST['id']
    	p_name = request.POST['name']
    	p_gender = request.POST['gender']
    	p_age = request.POST['age']
    	p_address = request.POST['address']
    	p_phone = request.POST['phone']
    	patient_info = ' '.join([p_name,p_gender,p_age,p_address,p_phone])
    	patient_dict.update({p_id:patient_info})
    	return patient_dict


@delete('/patient/<p_id>')
def delete_record(p_id):
	if p_id in patient_dict.keys():
		del(patient_dict[p_id])
	return patient_dict


run(host='localhost',port=4547)
