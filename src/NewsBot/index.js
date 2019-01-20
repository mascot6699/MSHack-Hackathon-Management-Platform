module.exports = async function(context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    const firebase = require('./firebase.js');
    const database = firebase.database();
    const https = require('https');

    if (req.query.source || (req.body && req.body.source)) {
        function bulkPostUpdation(article) {
            if(article && article.content){
                database.ref(`chat/trending/messages`).push({
                    sender: "News Bot",
                    sender_id: "news-bot",
                    message: article.content + ' : ' + article.url,
                    timestamp: new Date().toJSON()
                });
            }
        }

        context.res = {
            body: "Hello " + (req.query.source || req.body.source)
        } 
        https.get(`https://newsapi.org/v2/top-headlines?sources=${req.query.source}&apiKey=d597ae1941da4aef84b90adb1e964af1`, (resp) => {
            let data = '';

            // A chunk of data has been recieved.
            resp.on('data', (chunk) => {
                data += chunk;
            });

            // The whole response has been received. Print out the result.
            resp.on('end', () => {
                let articles = JSON.parse(data).articles;
                let articleIndex = Math.floor(Math.random() * articles.length); 
                let selectedArticle = articles[articleIndex];
                bulkPostUpdation(selectedArticle);
            });

        }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    } else {
        context.res = {
            status: 400,
            body: "Please pass a source on the query string or in the request body"
        };
    }
};