/**
 * 产品广告生成器 - React 组件版本
 * 
 * 这是一个基于 React 的产品广告生成器组件，使用 Gemini 2.0 Flash API
 * 来生成专业的产品广告图片。
 * 
 * 功能特性：
 * - 支持多种图片格式上传 (PNG, JPG, WEBP)
 * - 10种不同的广告场景选择
 * - 基于 Gemini AI 的图片生成
 * - 响应式设计，支持深色模式
 * - 错误处理和重试机制
 * 
 * 使用方法：
 * 1. 将此组件集成到 React 应用中
 * 2. 确保已安装必要的依赖：react, lucide-react, tailwindcss
 * 3. 配置 Gemini API 密钥
 * 
 * 作者：广东第二师范学院
 * 日期：2025年8月
 */

import React, { useState, useCallback } from 'react';
import { Upload, Wind, Image as ImageIcon, Newspaper, Bus, Tv, Coffee, Instagram, BrickWall, Landmark, Plane } from 'lucide-react';

// Main App Component
const App = () => {
    const [originalImage, setOriginalImage] = useState(null);
    const [generatedImage, setGeneratedImage] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [selectedAdFormat, setSelectedAdFormat] = useState(null);

    // List of 10 creative ad format ideas with corresponding icons
    const adFormats = [
        { id: 'billboard', text: 'A massive billboard in a bustling city center like Times Square.', icon: <Wind className="w-6 h-6" /> },
        { id: 'magazine', text: 'A full-page color advertisement in a glossy fashion magazine.', icon: <Newspaper className="w-6 h-6" /> },
        { id: 'bus', text: 'An ad on the side of a classic red double-decker bus in London.', icon: <Bus className="w-6 h-6" /> },
        { id: 'airport', text: 'A digital screen ad at a futuristic airport terminal.', icon: <Tv className="w-6 h-6" /> },
        { id: 'coffeeshop', text: 'A rustic wooden sign outside a cozy coffee shop on a cobblestone street.', icon: <Coffee className="w-6 h-6" /> },
        { id: 'social', text: 'A social media sponsored post on a popular influencer\'s feed.', icon: <Instagram className="w-6 h-6" /> },
        { id: 'vintage_poster', text: 'A vintage-style poster on a brick wall in a trendy alleyway.', icon: <BrickWall className="w-6 h-6" /> },
        { id: 'jumbotron', text: 'An advertisement on a jumbotron screen at a packed sports stadium.', icon: <Landmark className="w-6 h-6" /> },
        { id: 'movie_placement', text: 'A product placement on a table in a scene from a high-budget movie.', icon: <ImageIcon className="w-6 h-6" /> },
        { id: 'airplane_ad', text: 'An ad on the back of a seat on a commercial airplane.', icon: <Plane className="w-6 h-6" /> },
    ];

    // Handles the image file selection
    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setOriginalImage(reader.result);
                setGeneratedImage(null); // Clear previous generation
                setError(null);
            };
            reader.onerror = () => {
                setError("Failed to read the image file. Please try another one.");
            };
            reader.readAsDataURL(file);
        }
    };

    // Main function to call the Gemini API
    const generateAd = useCallback(async () => {
        if (!originalImage || !selectedAdFormat) {
            setError("Please upload an image and select an ad format first.");
            return;
        }

        setIsLoading(true);
        setError(null);
        setGeneratedImage(null);

        const base64ImageData = originalImage.split(',')[1];
        const prompt = selectedAdFormat.text;

        const payload = {
            contents: [{
                parts: [
                    { text: `Generate a photorealistic advertisement featuring the following product. Context: ${prompt}` },
                    {
                        inlineData: {
                            mimeType: "image/png",
                            data: base64ImageData
                        }
                    }
                ]
            }],
            generationConfig: {
                responseModalities: ['TEXT', 'IMAGE']
            },
        };

        const apiKey = ""; // API key will be injected by the environment
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent?key=${apiKey}`;

        try {
            // Exponential backoff for retries
            let response;
            let retries = 3;
            let delay = 1000;
            for (let i = 0; i < retries; i++) {
                response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    break;
                } else if (response.status === 429 || response.status >= 500) {
                    // Retry on rate limiting or server errors
                    await new Promise(resolve => setTimeout(resolve, delay));
                    delay *= 2;
                } else {
                    // Don't retry for other client-side errors
                    break;
                }
            }

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error?.message || `API request failed with status ${response.status}`);
            }

            const result = await response.json();
            const base64Data = result?.candidates?.[0]?.content?.parts?.find(p => p.inlineData)?.inlineData?.data;

            if (base64Data) {
                setGeneratedImage(`data:image/png;base64,${base64Data}`);
            } else {
                const textResponse = result?.candidates?.[0]?.content?.parts?.find(p => p.text)?.text;
                throw new Error(textResponse || "No image data found in the API response. The model may have refused the request.");
            }
        } catch (err) {
            setError(`An error occurred: ${err.message}`);
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    }, [originalImage, selectedAdFormat]);
    
    // Component for the image upload area
    const ImageUploader = () => (
        <div className="w-full lg:w-1/2 p-4 flex flex-col items-center justify-center border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-2xl text-center h-80 lg:h-auto">
            <label htmlFor="image-upload" className="cursor-pointer">
                <div className="flex flex-col items-center justify-center">
                    <Upload className="w-12 h-12 text-gray-400 dark:text-gray-500 mb-4" />
                    <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-300">Click to upload your product image</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-400">PNG, JPG, or WEBP</p>
                </div>
                <input id="image-upload" type="file" className="hidden" accept="image/png, image/jpeg, image/webp" onChange={handleImageChange} />
            </label>
        </div>
    );

    // Component to display the uploaded image
    const OriginalImageViewer = () => (
        <div className="w-full lg:w-1/2 p-4 flex flex-col items-center justify-center">
            <h3 className="text-xl font-semibold mb-4 text-gray-800 dark:text-gray-200">Your Product</h3>
            <div className="w-full aspect-square rounded-2xl overflow-hidden shadow-lg bg-gray-100 dark:bg-gray-800">
                <img src={originalImage} alt="Uploaded Product" className="w-full h-full object-contain" />
            </div>
        </div>
    );

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 font-sans p-4 sm:p-6 lg:p-8">
            <div className="max-w-7xl mx-auto">
                <header className="text-center mb-8">
                    <h1 className="text-4xl sm:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-500 to-pink-500">
                        Product Ad Generator
                    </h1>
                    <p className="mt-4 text-lg text-gray-600 dark:text-gray-400">
                        Upload your product and watch AI create stunning advertisements!
                    </p>
                </header>

                <main>
                    {/* Step 1: Image Upload */}
                    <div className="bg-white dark:bg-gray-800/50 p-6 rounded-3xl shadow-lg mb-8">
                        <h2 className="text-2xl font-semibold mb-4 flex items-center">
                            <span className="bg-purple-500 text-white rounded-full h-8 w-8 text-sm flex items-center justify-center mr-3">1</span>
                            Upload Your Image
                        </h2>
                        <div className="flex flex-col lg:flex-row gap-6">
                            {!originalImage ? <ImageUploader /> : <OriginalImageViewer />}
                             <div className="w-full lg:w-1/2 p-4 flex flex-col justify-center">
                                <h3 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-2">How it works:</h3>
                                <p className="text-gray-600 dark:text-gray-400">
                                    Our AI, powered by Gemini 2.5 Flash, takes your product image and seamlessly integrates it into a new, professionally generated ad scene based on your selection.
                                </p>
                                {originalImage && (
                                    <label htmlFor="image-upload" className="mt-4 inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 cursor-pointer">
                                        <Upload className="w-4 h-4 mr-2" />
                                        Change Image
                                        <input id="image-upload" type="file" className="hidden" accept="image/png, image/jpeg, image/webp" onChange={handleImageChange} />
                                    </label>
                                )}
                            </div>
                        </div>
                    </div>

                    {/* Step 2: Select Ad Format */}
                    {originalImage && (
                        <div className="bg-white dark:bg-gray-800/50 p-6 rounded-3xl shadow-lg mb-8">
                            <h2 className="text-2xl font-semibold mb-4 flex items-center">
                                <span className="bg-purple-500 text-white rounded-full h-8 w-8 text-sm flex items-center justify-center mr-3">2</span>
                                Select Ad Format
                            </h2>
                            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4">
                                {adFormats.map((format) => (
                                    <button
                                        key={format.id}
                                        onClick={() => setSelectedAdFormat(format)}
                                        className={`p-4 border-2 rounded-xl text-left transition-all duration-200 flex flex-col items-center justify-center text-center h-36 ${selectedAdFormat?.id === format.id ? 'border-purple-500 bg-purple-50 dark:bg-purple-900/20 ring-2 ring-purple-500' : 'border-gray-200 dark:border-gray-700 hover:border-purple-400 hover:bg-gray-50 dark:hover:bg-gray-700/50'}`}
                                    >
                                        <div className="mb-2 text-purple-500">{format.icon}</div>
                                        <p className="font-medium text-sm capitalize">{format.id.replace('_', ' ')}</p>
                                    </button>
                                ))}
                            </div>
                             {selectedAdFormat && (
                                <p className="mt-4 text-center text-gray-600 dark:text-gray-400 bg-gray-100 dark:bg-gray-700/50 p-3 rounded-lg">
                                    <strong>Selected:</strong> {selectedAdFormat.text}
                                </p>
                            )}
                        </div>
                    )}

                    {/* Step 3: Generate Ad */}
                    {originalImage && selectedAdFormat && (
                        <div className="text-center mb-8">
                            <button
                                onClick={generateAd}
                                disabled={isLoading}
                                className="px-8 py-4 bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold rounded-full shadow-lg hover:scale-105 transform transition-transform duration-300 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed disabled:scale-100"
                            >
                                {isLoading ? 'Generating Your Ad...' : '✨ Generate Ad'}
                            </button>
                        </div>
                    )}

                    {/* Display Area for Result */}
                    {error && <div className="text-center p-4 mb-8 bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-300 rounded-lg">{error}</div>}
                    
                    <div className="w-full p-4 flex flex-col items-center justify-center">
                        {isLoading && (
                            <div className="w-full max-w-2xl aspect-video bg-white dark:bg-gray-800/50 rounded-2xl shadow-lg flex flex-col items-center justify-center text-center p-8">
                                <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-purple-500 mb-4"></div>
                                <p className="text-lg font-semibold text-gray-700 dark:text-gray-300">AI is creating magic...</p>
                                <p className="text-sm text-gray-500 dark:text-gray-400">This can take a moment. Please wait.</p>
                            </div>
                        )}
                        {generatedImage && (
                             <div className="w-full max-w-4xl">
                                <h2 className="text-3xl font-bold text-center mb-4">Your Generated Ad!</h2>
                                <div className="w-full aspect-video rounded-2xl overflow-hidden shadow-2xl bg-gray-100 dark:bg-gray-800 ring-2 ring-purple-500/50">
                                    <img src={generatedImage} alt="Generated Ad" className="w-full h-full object-contain" />
                                </div>
                             </div>
                        )}
                    </div>
                </main>
            </div>
        </div>
    );
};

export default App;
