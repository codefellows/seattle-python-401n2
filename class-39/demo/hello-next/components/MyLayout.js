/*
compose Header
define a layoutStyle
    margin 20 pixels
    padding 20 pixels
    border 1 pixel solid #DDD
Define a Layout component
    styled div
    Header
    props.children

Export Layout

*/

import Header from './Header';

const layoutStyle = {
    margin: 20,
    padding: 20,
    border: '1px solid #DDD',
}

export default props => (
    <div style={layoutStyle}>
        <Header />
        {props.children}
    </div>
)

