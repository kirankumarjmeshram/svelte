/**
 * This hook captures every request passing through the application. 
 * Using the handle function, we access the cookies set previously, 
 * determine whether the user should be redirected, and set the user store again.
 * 
 *  Note the use of event.locals to pass user data through server-side functions with the request.
 */

import {redirect} from "@sveltejs/kit"

// define the routes of we want to be possible to access without auth
const public_path = [
    '/signup',
    '/signin'
];

// function to verify if the request path is inside the public_paths array
function isPathAllowed(path) {
    return public_path.some(allowedPath =>
        path === allowedPath || path.startsWith(+'/')
    )
}

export const handle = async ({event, resolve}) =>{
    let user = null;
    // check if the cookie exist, and if exists, parse it to the user variable
    if(event.cookies.get('user') !== undefined && event.cookies.get('user') !== null) {
        user = JSON.parse(event.cookies.get('user'))
    }
    
    const url = new URL(event.request.url);

    // validate the user existence and if the path is acceesible
    if(!user && !isPathAllowed(url.pathname)) {
        throw redirect(302, '/signin')
    }

    if(user) {
        //set the user to the locals
        event.locals.user = user;

        // redirect user if he is already logged if he try to access signin or signup
        if(url.pathname === '/signup' || url.pathname === '/signin') {
            throw redirect(302,'/')
        }
    }

    const response = await resolve(event);

    return response;




}