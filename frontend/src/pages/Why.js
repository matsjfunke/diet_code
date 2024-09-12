import React from "react";
import "./Why.css";
import points from "../assets/why-delete.json";
import { Light as SyntaxHighlighter } from "react-syntax-highlighter";
import { nightOwl } from "react-syntax-highlighter/dist/esm/styles/hljs";
import javascript from "react-syntax-highlighter/dist/esm/languages/hljs/javascript";
import python from "react-syntax-highlighter/dist/esm/languages/hljs/python";

SyntaxHighlighter.registerLanguage("javascript", javascript);
SyntaxHighlighter.registerLanguage("python", python);

function Why() {
  const getYoutubeVideoId = (url) => {
    const regExp =
      /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);
    return match && match[2].length === 11 ? match[2] : null;
  };

  const renderContent = (item) => {
    switch (item.type) {
      case "text":
        return (
          <p>
            <strong>{item.content}</strong>
          </p>
        );
      case "link":
        const videoId = getYoutubeVideoId(item.content);
        if (videoId) {
          return (
            <div className="video-thumbnail">
              <a href={item.content} target="_blank" rel="noopener noreferrer">
                <img
                  src={`https://img.youtube.com/vi/${videoId}/0.jpg`}
                  alt={item.text}
                />
                <div className="play-button"></div>
              </a>
              <p>
                <strong>{item.text}</strong>
              </p>
            </div>
          );
        } else {
          return (
            <a href={item.content} target="_blank" rel="noopener noreferrer">
              <strong>{item.text}</strong>
            </a>
          );
        }
      case "code":
        return (
          <div className="code-block">
            <p>
              <strong>{item.text}</strong>
            </p>
            <SyntaxHighlighter
              language={item.language}
              style={nightOwl}
              showLineNumbers={true}
              wrapLines={true}
              wrapLongLines={true}
            >
              {item.code}
            </SyntaxHighlighter>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="why-page">
      <h1 className="main-heading">Why Delete Code?</h1>
      <div className="points-container">
        {points.map((point, index) => (
          <div key={index} className="point-box">
            {renderContent(point)}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Why;
