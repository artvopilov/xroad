use test;

db.createCollection('user');
db.user.insertOne({
    username: 'monsta',
    password: '$2b$12$DpliKadOwzjZjxHlB9P5rOP9b6Bm0vZK.M13fXg7hZ8wmaWyZmfj.',
    user_typ: 'person',
    name: 'Artem',
    phone: '+79811434975',
    gender: 'male',
    age: 25
});
