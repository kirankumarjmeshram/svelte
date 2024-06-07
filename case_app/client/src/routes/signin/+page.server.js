import { user } from "$lib/stores/user.js";
import { redirect } from "@sveltejs/kit";

export const actions = {
    default: async ({cookies, request, fetch}) => {
        const data = await request.formData();
        const email = data.get('email');
        const password = data.get('password');

        if(typeof email !== 'string' || typeof password !== 'string' || !email || !password ) {
            return {
                status: 400,
                body: {
                    success:false,
                }
            }
        }

        const response = await fetch('http://127.0.0.1:3000/users/sign_in', {
            method:'POST', 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                    email,
                    password
            })
        })

        if(response.ok) {
            const data = await response.json()
            cookies.set('user', JSON.stringify(data.user),{path:'/'})
            cookies.set('jwt', response.headers.get('Authorization'), {path: '/'})
            let obj = {
                ...data,
                jwt: response.headers.get('Authorization')
            }

            user.set(obj)
            // console.log(obj)
            // let userdata;
            // user.subscribe((value)=>{
            //     userdata = value
            // })
            // console.log("userdata2",userdata)
            

            throw redirect(302, '/')
        }else{
            const {error} = await response.json()
            return {
                status: 400,
                body: {
                    success: false,
                    error
                }
            }
        }
    }
}