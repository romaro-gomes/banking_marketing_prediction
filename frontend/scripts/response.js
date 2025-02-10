const submitButton = document.getElementById('submit');

async function predict(event){

    event.preventDefault();

    const formData = {
        age: document.getElementById('age').value,
        job: document.getElementById('job').value,
        marital: document.getElementById('marital').value,
        education: document.getElementById('education').value,
        default: document.getElementById('default').value,
        balance: document.getElementById('balance').value,
        housing: document.getElementById('housing').value,
        loan: document.getElementById('loan').value,
        contact: document.getElementById('contact').value,
        day: document.getElementById('day').value,
        month: document.getElementById('month').value,
        duration: document.getElementById('duration').value,
        campaign: document.getElementById('campaign').value,
        pdays: document.getElementById('pdays').value,
        previous: document.getElementById('previous').value,
        poutcome: document.getElementById('poutcome').value
    };


    const response = await fetch("http://127.0.0.1:8000/client/", {
        method: "POST",
        headers:{
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(formData)
    });

    if (!response.ok){
        throw new Error("Server don't response")
    }

    const predict = await response.json()
    const prediction = predict.prediction

        
    const predictArea = document.getElementsByClassName('response')[0];

    
    const predictValue =`<p class='prediction'>${prediction}</p>`
    
        
    predictArea.innerHTML= predictValue
}

submitButton.addEventListener('click',predict);

