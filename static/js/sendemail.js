//Here is my Send Email Script for my contact modal form. 
//To create this script i used the EmailJS documentation and what i came accross in one of the code institute teaching modules.

//Here is a list of URL that helped me create this JS Script.
//https://dashboard.emailjs.com/admin/integration/browser
//https://www.emailjs.com/docs/sdk/send/
//https://jsfiddle.net/api/post/library/pure/ - This code is from the playground test features within EmailJS and might not work since you have to login with my user details.

//Creating a variable btn to store the send button in the contact form so that the inner text can be changed at certain points.
let btn = document.getElementById('send-btn');

//This function is for the timing event used below and it is used to change btn text to Send.
function changeSendBtnText() {
    btn.textContent = 'Send';
}

//This function here is for the timing event below and is used to reset the contact form.
function resetForm() {
    document.getElementById('cookbook-contact-form').reset();
}

//This block of code here is for the overall EmailJS and was taken from the testing playround 
//of EmailJS and then modified to my needs. The top section adds an event listener to the forms
//submit button and once clicked it will change the button text to sending.
document.getElementById('cookbook-contact-form')
    .addEventListener('submit', function (event) {
        event.preventDefault();

        btn.textContent = 'Sending...';

        //These two variables store two very important details and these are needed for the next part 
        //to actually send the an email with EmailJS
        let serviceID = 'ifti-khan-portfolio';
        let templateID = 'ms3-cookbook-template';

        //Here is a promise method, as you can see the two variables above are used and below 
        //them is the template parameters of my email template that are assigned the value of 
        //the input fields of my general question contact form.
        emailjs.send(serviceID, templateID, {
                "modal_fullname": this.modal_name.value,
                "modal_username": this.modal_username.value,
                "modal_email": this.modal_email.value,
                "modal_message_subject": this.modal_message_sub.value,
                "modal_message": this.modal_message.value,

            })
            //Here is the response object which contains the status and text properties and this 
            //will show in the console of the browser as 200 for status and OK for text. 
            //I have also added a button text change to sent once the message has been send and 
            //for an alert window to open informing users that the message has been sent. 
            //The timing event uses the function above and changes the text back to send and resets 
            //the form.
            .then((response) => {
                btn.textContent = 'Sent';
                console.log("Message Has Been Sent", response.status, response.text);
                alert('Your message has been sent!');
                resetForm();
                setTimeout(changeSendBtnText, 3000);

                //Here is the error object and if there is an error it will display that in the console 
                //of the browser informing of the error. As well as changing the button text to error and 
                //opening an alert window to the user infroming them that there was an error. 
                //The timing event uses the function above and changes the text back to send and resets 
                //the form.
            }, (error) => {
                btn.textContent = 'Error';
                console.log("Message Failed To Send", error);
                alert(`Oops something went wrong!`);
                resetForm();
                setTimeout(changeSendBtnText, 3000)

            });
    });