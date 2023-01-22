// Loads in the AWS SDK
const AWS = require('aws-sdk'); 

// Creates the document client specifing the region 
// The tutorial's table is 'in us-east-1'
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'}); 

exports.handler = async (event, context, callback) => {
    // Handle promise fulfilled/rejected states
    await readMessage().then(data => {
        data.Items.forEach(function(item) {
            console.log(item.message)
        });
        callback(null, {
            // If success return 200, and items
            statusCode: 200,
            body: data.Items,
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
        })
    }).catch((err) => {
        // If an error occurs write to the console
        console.error(err);
    })
};

// Function readMessage
// Reads 10 messages from the DynamoDb table Message
// Returns promise
function readMessage() {
    const params = {
        TableName: 'Message',
        Limit: 10
    }
    return ddb.scan(params).promise();
}