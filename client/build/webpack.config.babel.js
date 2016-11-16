import path from 'path';
import webpack from 'webpack';
import autoprefixer from 'autoprefixer';

const SRC_DIR = path.join(__dirname, '../src');

export default { 
    devtool: 'source-map',
    entry: [
        'babel-polyfill',
        'webpack-dev-server/client?http://0.0.0.0:3000',
        'webpack/hot/dev-server',
        './src/index'
    ],
    output: {
        path: path.join(__dirname, '../dist'),
        filename: 'bundle.js',
        publicPath: '/static/'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin()
    ],
    module: {
        loaders: [{
            test: /\.jsx?$/,
            loaders: [
                'babel'
            ],
            include: SRC_DIR,
            exclude: /node_modules/
        }, {
          test: /\.css$/,
          loader: 'style-loader!css-loader'
        }]
    }
};
