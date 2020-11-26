import Link from 'next/link';

const headerStyle = {
    marginRight: 15
}


export default () => (
    <div>
        <Link href="/">
            <a style={headerStyle}>Home</a>
        </Link>
        <Link href="/about">
            <a style={headerStyle}>About</a>
        </Link>
    </div>
)
