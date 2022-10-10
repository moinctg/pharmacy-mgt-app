import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

const AddDoctor = () => {







    const { register, handleSubmit, reset } = useForm()

    const onSubmit = data => {


        fetch('http://127.0.0.1:8000/api/doctor/', {
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
            <h1 className='text-info my-4'>Add A New Doctor Info !</h1>
            <form onSubmit={handleSubmit(onSubmit)} className='shadow p-4'>
                <input {...register("name", { required: true, maxLength: 30 })} placeholder="Name" className='input-apply' />
                <br /><br />
                <input {...register("address", { required: true, maxLength: 200 })} placeholder="address" className='input-apply' />
                <br /><br />
                <input {...register("contact", { required: true, maxLength: 20 })} placeholder="contact" className='input-apply' />
                <br /><br />
                <input type="number" {...register("hospital_id", { required: true, maxLength: 20 })} placeholder="contact" className='input-apply' />
                <br /><br />
                

                <input style={{ backgroundColor: 'gold', color: 'blue', borderRadius: '20px', marginTop: '20px', padding: '10px' }} type="submit" />
            </form>

        </div>
    );
};

export default AddDoctor;