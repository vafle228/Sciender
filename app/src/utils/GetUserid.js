import { ID_NAME } from '@/utils/constants';

export default {
    name: "UseridMixin",

    computed: {
        id() { return +localStorage.getItem(ID_NAME); }
    },
}