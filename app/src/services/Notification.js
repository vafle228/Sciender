export default {
    warnNotification() { },
    
    errorNotification(error) { 
        console.error(error);
    },
    
    confirmNotification(message) {
        console.log(message);
    },
}