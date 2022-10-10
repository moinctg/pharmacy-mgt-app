import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
const AddPaitent = () => {
    const { register, handleSubmit, reset } = useForm()

    const onSubmit = data => {
        fetch('http://127.0.0.1:8000/api/patient/', {
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
        return (
            <div>
                <h1 className='text-info my-4'>Add A New Product !</h1>
                <form onSubmit={handleSubmit(onSubmit)} className='shadow p-4'>
                    <input {...register("name", { required: true, maxLength: 30 })} placeholder="Name" className='input-apply' />
                    <br /><br />
                    <input {...register("address", { required: true, maxLength: 200 })} placeholder="address" className='input-apply' />
                    <br /><br />
                    
                    <select {...register("gender", { required: true })}>
                        <option value="">Select...</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                    </select><br /><br />
                    <input {...register("contact", { required: true, maxLength: 20 })} placeholder="contact" className='input-apply' />
                    <br /><br />

                    <textarea {...register("details")}
                        className='input-apply'
                        placeholder="Details" /><br /><br />
                   
                    <select {...register("doctor_id", { required: true })}>
                        <option value="">Select Doctor</option>
                        <option value="1">abdul hoq</option>
                        <option value="2">md sobuj</option>
                        <option value="3">md sahmim</option>
                        <option value="4">md korim</option>
                    </select><br /><br />

                    <input style={{ backgroundColor: 'gold', color: 'blue', borderRadius: '20px', marginTop: '20px', padding: '10px' }} type="submit" />
                </form>

            </div>
        );
    };

    export default AddPaitent;