require("dotenv").config({path: "../app/.env"})

conn = new Mongo(`mongodb://${process.env.ME_CONFIG_MONGODB_ADMINUSERNAME}:${process.env.ME_CONFIG_MONGODB_ADMINPASSWORD}@localhost:27017`);
db = conn.getDB("AFTERHOURS");

db.userss.deleteMany({})

db.userss.insertMany([
   {
    username: 'raaaa raaaa',
    email: 'goob@gmail.com',
    phone: null,
    fullname: 'silly silly',
    hashedPassword: 'bl@hbl@h101',
    lastLogin: null,
    huntHistory: []
   },
   {
    username: 'looneys',
    email: 'turferson@gmail.com',
    phone: null,
    fullname: 'Turferson cstoner',
    hashedPassword: 'strawberry+martini2',
    lastLogin: null,
    huntHistory: []
   },
   {
      username: 'Rosserson',
      email: 'friends@gmail.com',
      phone: null,
      fullname: 'Chandler Bing',
      hashedPassword: 'Pheobe4ever!',
      lastLogin: null,
      huntHistory: []
   },
   {
      username: 'poppy_flowers',
      email: 'flowers@gmail.com',
      phone: null,
      fullname: 'Rose Daisy',
      hashedPassword: 'heyThereDelil@h1',
      lastLogin: null,
      huntHistory: []
   },
   {
      username: 'newman',
      email: 'seinfeld@gmail.com',
      phone: null,
      fullname: 'elaine benes',
      hashedPassword: 'george*costanza4',
      lastLogin: null,
      huntHistory: []
   },
] )
printjson( db.userss.find( {} ) );