db.createUser({
    user: 'jon',
    pwd: 'password',
    customData: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
})

// db.getUsers()      ----will show all users
// db.dropUser('Jon')   ----will remove the user seleced
// db.getUsers()      ----will show all users
// db.dropUser('Jon')   ----will remove the user seleced
// db.createCollection('books')   --returns the json object key is okay and value is 1--in the api environment example you can return pure json


// -------------------------------------------------------------


db.books.insert({
    "title": "OOP Programming",
    "startDate": new Date(),
    "authors": [
        { "name": "Jon Snow Jr" },
    ]
})

// expecting an object everything has to be passed in with curly braces

// db.books.insert ({ })
// to pass in a collection for multiple authors pass in as an array 
// "authors": [
//     { "name": "Jon Snow Jr"},
// ]


// -------------------------------------------------------------


// insertMany   takes in an array so use ( [ ] )  not curly brackets 
// insertMany gives you a different return value
// it will return acknowledged true and returned the id of the object-a hash value-unique structure


db.books.insertMany([
    {
        "name": "Confident Ruby",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Avdi Grim" }
        ]
    },
    {
        "name": "The War of Art",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Steven Pressfield" }
        ]
    },
    {
        "name": "Blink",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Malcolm Gladwell" }
        ]
    }
])


// ----------------------------------------------------------


db.books.find(
    {
        name: "Confident Ruby"
    },
    {
        _id: 0,
        name: 1,
        authors: 1
    }
).pretty()

// insertMany   takes in an array so use ( [ ] )  not curly brackets 
// insertMany gives you a different return value
// it will return acknowledged true and returned the id of the object-a hash value-unique structure
// projects are onstraints that return elements that you want
// projections***


db.books.insert({
    "name": "Deep Work: Rules for Focused Success in a Distracted World",
    "publishedDate": new Date(),
    "authors": [
        {"name": "Call Newport"}
    ]
});


// --------------------------------------------------------------------



db.books.insert({
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Malcolm Gladwell", "active": "true" },
        { "name": "Ghost Writer", "active": "true" }
    ]
});


db.books.find(
    {
        name: "Blink"
    },
    {
        name: 1,
        publishedDate: 1,
        "authors.name": 1
    }
).pretty()



// --------------------------------------------------------



db.books.find({name: "blink"})



// --------------------------------------------------------



db.books.insert(
    {
    "name": "Deep Work: Rules for Focused Success in a Distraced World",
    "publishedDate": new Date(),
    "reviews": 100,
    "authors": [
        {"name": "Cal Newport"}
        ]
    }
)


// ------------------------------------------------------

// //this is how we create a user in the mongo database 
// // then below it is creating a books collection database

// db.createUser({
//     user: 'Benjamin',
//     pwd: 'password',
//     customData: { startDate: new Date() },
//     roles: [
//         { role: 'clusterAdmin', db: 'admin' },
//         { role: 'readAnyDatabase', db: 'admin' },
//         'readWrite'
//     ]
// })
// //to view all is db.getUsers()
// //to drop user you run db.dropUser('name to delete')

// db.books.insert({
//     "name": "OOP Programming",
//     "publishedDate": new Date(),
//     "authors": [       //an array of data here
//       { "name": "Jon Snow jr"}, //expects to recieve an object pass in with curly
//     ]
// }) 





// db.books.insertMany([   //insert many takes an array
//     {
//         "name": "Confident Ruby",
//         "publishedDate": new Date(),
//         "authors": [
//             { "name": "Avdi Grimm" }
//         ]
//     },
//     {
//         "name": "Python Rocks",
//         "publishedDate": new Date(),
//         "authors": [
//             { "name": "Benjamin Nicklaus" }
//         ]
//     },
//     {
//         "name": "Python Broski",
//         "publishedDate": new Date(),
//         "authors": [
//             { "name": "Ben and J" }
//         ]
//     },
// ])
// //mongo returns a hash value for the id-so it is unique
// // to retrieve certain values/components back use 1's and 0's
// // 1 is what you want and 0 is what you not want
// // to limit what is returned below
// db.books.find(
//     {
//         name: "Confident Ruby"
//     },
//     {
//         _id: 0,
//         name: 1,
//         publishedDate: 1,
//         authors: 1
//     }
// ).pretty()




// // How to Query for a Portion of a String
// //inserting a new book
// //implementing a regualr expression
// //db.books.findOne({ name: /.deep work./i }) when you see text in between slashes means reg exp
// //regardless match what ever matches deep work for example
// // the i means it is making it case insensetive 

// db.books.insert({
//     "name": "Deep Work: Rules for Focused Success in a Distracted World",
//     "publishedDate": new Date(),
//     "authors": [
//         {"name": "cal Newport"}
//     ]
// });

// // How to Delete Documents 
// db.books.remove({name: "OOP Programming"}, 1) //remove one item passing in an explicit number to be removed




// //How to Include Nested Fields in a find Query
// //ability to query document don't care if active
// //starting code below
// db.books.insert({
//   "name": "Blink",
//   "publishedDate": new Date(),
//   "authors": [
//       { "name": "Malcome Gladwell", "active": "true"},
//       { "name": "Ghost Writer", "active": "true"}
//   ]
// });
// //adjusted code from above
// query the document but don't care if the author is active
// db.books.find(
//     {
//         name: "Blink"
//     },
//     {
//         name: 1,
//         publishedDate: 1,
//         "authors.name": 1,  //authors is the array with all the objects-mongo goes into array and brings back name attribute
//     }
// )
// //How to check if field exists in a document
// db.books.insert( 
//     {
//       "name": "Deep Work: Rules for Focused Success in a Distracted World",
//       "publishedDate": new Date(),
//       "reviews": 100,
//       "authors": [
//         {"name": "Cal Newport"}
//       ]
//     }
//   )
// //to run the query there is a specific function
// //use the commands below 
//   // db.books.find({ reviews: { $exists: true } })     if it has the values
//   // db.books.find({ reviews: { $exists: false } })    if it doesn't have the values
//   //could be used to clean the databases

