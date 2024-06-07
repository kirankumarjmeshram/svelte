import {redirect} from '@sveltejs/kit'

export const actions = {
    default: async ({cookies}) => {
        cookies.set('user', null, {path:'/'})
        throw redirect(302, '/');
    }
}