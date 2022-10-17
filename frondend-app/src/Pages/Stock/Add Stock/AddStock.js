import React from 'react';

const AddStock = () => {
    const AddPaitent = () => {
        const { register, handleSubmit, reset } = useForm()
    
        const onSubmit = data => {
            fetch('http://127.0.0.1:8000/api/stock/', {
                    method: "POST",
                    headers: { "content-type": "application/json" },
                    body: JSON.stringify(data),
                  })
                    .then((res) => res.json())
                    .then((data) => {
                      console.log(data);
                      if (data.insertedId) {
                        alert("add hoise broooo ");
                      }
                    //   } else {
                    //     alert("add korte pari nai");
                        reset()
                    
                    });
            
            }
        }
    return (
        <div>
            

            <div className='main-container'>
            
             
            <div className='container position-absolute top-50 start-50'>
                <div className='row'>
                    <div classsname="col-md-6">
 
    
     
                  <h1 className='text-success my-4'>Add A New Stock !</h1>
                <form onSubmit={handleSubmit(onSubmit)} className='p-5'>
                <input  type="number" {...register("price", { required: true, maxLength: 30 })} placeholder="price" className='input-apply' />
                    <br /><br />
                    <input type="number" {...register("quntity", { required: true, maxLength: 200 })} placeholder="quntity" className='input-apply' />
                    <br /><br />
                    <input type="number" {...register("waranty", { required: true, maxLength: 200 })} placeholder="quntity" className='input-apply' />
                    <br /><br />
                  <Controller
        control={control}
        name="dateInput"
        render={({ field }) => (
          <DatePicker
            placeholderText="Select date"
            onChange={(date) => field.onChange(date)}
            selected={field.value}
          />
        )}
      />
      {errors.dateInput && <span>This field is required</span>}
      <br /><br />
                    <input {...register("name", { required: true, maxLength: 30 })} placeholder="Name" className='input-apply' />
                    <br /><br />
                    <input type="number" {...register("quntity", { required: true, maxLength: 200 })} placeholder="quntity" className='input-apply' />
                    <br /><br />
                    <input type="number" {...register("price", { required: true, maxLength: 20 })} placeholder="price" className='input-apply' />
                    
                    <br /> <br/>
                   
                  <select {...register("manafucture", { required: true })}>
                        <option value="">Select... company</option>
                        <option value="Square ">Square </option>
                        <option value="Ibne Sina">Ibne Sina</option>
                        <option value="Beximco">Beximco   </option>
                        <option value="Incepta ">Incepta  </option>
                        <option value="Healthcare  ">Healthcare   </option>
                        <option value="ACI  ">ACI   </option>
                     
                    </select><br />
                    <Controller
        control={control}
        name="dateInput"
        render={({ field }) => (
          <DatePicker
            placeholderText="Select date"
            onChange={(date) => field.onChange(date)}
            selected={field.value}
          />
        )}
      />
      {errors.dateInput && <span>This field is required</span>}
      <br /><br />
{/* 
                    <textarea {...register("details")}
                        className='input-apply'
                        placeholder="Details" /><br /><br />
                   
                    <select {...register("doctor_id", { required: true })}>
                        <option value="">Select Doctor</option>
                        <option value="1">abdul hoq</option>
                        <option value="2">md sobuj</option>
                        <option value="3">md sahmim</option>
                        <option value="4">md korim</option>
                    </select><br /><br /> */} 

                    <input style={{ backgroundColor: 'gold', color: 'blue', borderRadius: '20px', marginTop: '20px', padding: '10px' }} type="submit" />
                </form>
            
        </div>
        </div>
        </div>
        </div>
            
        </div>
    );
};

export default AddStock;