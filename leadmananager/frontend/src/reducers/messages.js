import { CREATE_MESSAGE } from '../actions/types';

const initalState = {
    msg: {},
    status: null
}
export default function (state = initalState, action) {
    switch (action.type) {
        case CREATE_MESSAGE:
            return (state = action.payload)
            break;
        default:
            return state;
    }
};