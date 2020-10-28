const MiniCssExtractPlugin = require("mini-css-extract-plugin")
const BundleTracker = require('webpack-bundle-tracker')
const appName = 'app'
const path = require("path")


module.exports = {
    entry: {
        app: './' + appName + '/static/js/index_app.js',
    },
    output: {
        path: path.resolve('./' + appName + '/static/bundles/'),
        filename: '[name]-[hash].js',
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: './webpack-stats.json'
        }),
        new MiniCssExtractPlugin({
            filename: '[name]-[hash].css',
            chunkFilename: '[id].css',
        }),
    ],
    module: {
        rules: [{
                test: /\.scss$/,
                use: [{
                        loader: MiniCssExtractPlugin.loader,
                    },
                    {
                        loader: "css-loader"
                    },
                    {
                        loader: "sass-loader",
                    }
                ]
            },
            {
                test: /\.css$/,
                use: ['css-loader']
            }
        ]
    }
}
