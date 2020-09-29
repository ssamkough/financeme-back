import express from 'express';
const apiRouter = express.Router();

const wrapAsync = (fn) => {
    return (req, res, next) => {
        fn(req, res, next).catch(next);
    };
};

apiRouter.get('/', (req, res) => {
    // res.redirect('https://[postman-link]');
    res.send('API Documentation');
});

export default apiRouter;
