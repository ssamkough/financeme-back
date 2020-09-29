"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const router_1 = __importDefault(require("./router"));
const app = express_1.default();
app.use('/api', router_1.default);
app.get('/', (req, res) => {
    const fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl + 'api';
    res.status(200).send('<a href="' + fullUrl + '">' + fullUrl + '</a>');
});
const onAppStarted = () => {
    console.log(`App running on ${port}.`);
};
const port = parseInt(process.env.PORT) || 8000;
app.listen(port, onAppStarted);
//# sourceMappingURL=app.js.map